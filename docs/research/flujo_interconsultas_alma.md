---
title: Flujo de Interconsultas en ALMA/TrakCare
date: 2026-02-26
status: investigacion-activa
impacts:
  - docs/library/scripts.md
  - CHANGELOG.md
tags: [interconsulta, consultoria-llamado, teleconsulta, evaluacion, HOVA, OE_OrdItem, PA_EnquiryContact]
---

# Flujo de Interconsultas en ALMA/TrakCare

## Resumen Ejecutivo

Las interconsultas internas en ALMA/TrakCare se implementan a traves del modulo de
Order Entry (OE_OrdItem) usando items del catalogo ARC_ItmMast con prefijo **HOVA***.
El ruteo al medico receptor se hace via grupos de usuario (`ITM2_Group_DR` en OE_OrdItem2).

**Descubrimiento clave**: El formulario de respuesta/asignacion es **PA_EnquiryContact**
("Datos de Contacto"), con 2,103 registros activos. Todos vinculados a ordenes
via `ENQ_OEOrdItem_DR`. El estado de la orden transita:
**Inactivo (5) -> Solicitado (12) -> Ejecutado (3)** via `OE_OrdStatus`.

## Catalogos Encontrados

### Interconsultas Internas (51 items)
- Codigos: HOVA0001 - HOVA0040 + HOVA00101-HOVA00103 + otros
- Ejemplo: `HOVA0003` = "INTERCONSULTAS INTERNAS A NEUROLOGIA ADULTO"
- Tabla: `SQLUser.ARC_ItmMast` WHERE `ARCIM_Code LIKE 'HOVA%' AND ARCIM_Desc LIKE '%INTERCONSULTA%'`

### Consultorias de Llamado (13 items)
- Codigos: HOVA0049-HOVA0055, HOVA0112-HOVA0114, HOVA00130-HOVA00132
- Ejemplo: `HOVA0055` = "CONSULTORIA DE LLAMADO NEUROLOGIA ADULTO"
- Tabla: `SQLUser.ARC_ItmMast` WHERE `ARCIM_Desc LIKE '%CONSULTORIA%LLAMADO%'`

### Teleconsultas (48 items)
- Codigos: 0108*
- Tabla: `SQLUser.ARC_ItmMast` WHERE `ARCIM_Desc LIKE '%TELECONSULTA%'`

### Evaluaciones (102 items)
- Tabla: `SQLUser.ARC_ItmMast` WHERE `ARCIM_Desc LIKE '%EVALUACION%'`

## Modelo de Datos - Flujo Completo

```
1. ORDEN (creacion)
   ARC_ItmMast (HOVA*)
       |
       v
   OE_OrdItem  (OEORI_ItmMast_DR -> ARC_ItmMast)
       |
       +--> OE_OrdItem2  (ITM2_Group_DR -> SS_Group)   [grupo receptor]
       |
       +--> Region_CLXX_Misc_User.OEOrdItem             [decorator regional]
       |    (COEORI_GES, COEORI_No, COEORI_Verified, COEORI_Date)
       |
       +--> OE_OrdStatus  (ST_Status_DR -> OEC_OrderStatus)  [historial de estados]
            Step 1: Status 5 = "Inactivo"   (orden creada)
            Step 2: Status 12 = "Solicitado" (orden verificada, aparece en worklist)
            Step 3: Status 3 = "Ejecutado"   (IC respondida)

2. WORKLIST (asignacion)
   Region.CLXX.Model.EPVisitNumber.ClinicWorkList.LTInterconsultasInternas
       |
       +--> Menu: "Solicitudes Clinicas" > "Lista IC internas"
       +--> Menu: "Interconsultas Sin Asignar" (CLXX.ICInternasSol)
       +--> Menu: "Interconsultas Asignadas"   (CLXX.ICInternasAsig)

3. FORMULARIO "DATOS DE CONTACTO" (respuesta)
   PA_EnquiryContact  (2,103 registros, TODOS con ENQ_OEOrdItem_DR vinculado)
       |
       +--> ENQ_OEOrdItem_DR      -> OE_OrdItem          [orden IC]
       +--> ENQ_Hospital_DR       -> CTHospital           [establecimiento]
       +--> ENQ_Location_DR       -> CTLoc                [local/servicio]
       +--> ENQ_CTCP_DR           -> CTCareProv           [profesional asignado]
       +--> ENQ_Date / ENQ_Time                           [fecha/hora contacto]
       +--> ENQ_RequestStatus_DR  -> PAC_RequestStatus    [estado solicitud]
       +--> ENQ_ContMethod_DR     -> PAC_ContMethod       [metodo contacto]
       +--> ENQ_Duration                                  [duracion en minutos]
       +--> ENQ_ConsultCateg_DR   -> OECConsultCateg      [categoria consulta]

4. RESPUESTA CLINICA
   MR_Encounter  (ENC_MRAdm_DR -> episodio, ENC_CareProv_DR -> medico)
       |
       +--> MR_SubjectFindings  (Subjetivo)
       +--> MR_ObjFind          (Objetivo)
       +--> MR_Evolution         (Evolucion)
       +--> MR_Diagnos           (Diagnosticos)
```

## Catalogos de Estados y Metodos

### OEC_OrderStatus (13 estados de orden)

| ID | Codigo | Descripcion | Uso IC |
|----|--------|-------------|--------|
| 1 | CO | Cajero | - |
| 2 | D | Suspendido | Cancelacion |
| **3** | **E** | **Ejecutado** | **IC completada** |
| 4 | H | En Espera | - |
| **5** | **I** | **Inactivo** | **Estado inicial** |
| 6 | IP | En Atencion | - |
| 7 | P | Pre-Orden | - |
| 8 | PO | Orden post-operatoria | - |
| 9 | Q | En Cola | - |
| **10** | **S** | **Agendado** | Algunas IC |
| 11 | U | No Verificado | - |
| **12** | **V** | **Solicitado** | **En worklist** |
| 13 | W | Lista de Espera | - |

### PAC_RequestStatus (3 estados de solicitud en PA_EnquiryContact)

| ID | Codigo | Descripcion |
|----|--------|-------------|
| 1 | 03 | Asignada |
| 2 | 02 | Finalizada |
| 3 | 01 | En Proceso |

### PAC_ContMethod (3 metodos de contacto)

| ID | Codigo | Descripcion |
|----|--------|-------------|
| 1 | 03 | Correo Electronico |
| 2 | 01 | WhatsApp |
| 3 | 02 | Telefonico |

## Grupos de Usuario Receptores (15 distintos)

| ID  | Codigo                                          | Uso |
|-----|------------------------------------------------|-----|
| 355 | CLXX.IP.Medico Hospitalizado                    | Mas comun |
| 47  | CLXX.IP.Medico Hospitalizado SM                 | |
| 48  | CLXX Medico Interconsultor                      | Grupo especifico IC |
| 211 | CLXX.OP.Medico Especialidades Ambulatorio        | |
| 289 | CLXX.IP.Medico Hospitalizado G-O                | |
| 160 | CLXX.IP.Medico Hospitalizacion Domiciliaria      | |
| 257 | CLXX.IP.Matrona Hospitalizado                    | |
| 122 | CLXX.IP.Medico Cuidados Criticos Neo             | |
| 128 | CLXX.IP.Medico Cuidados Criticos                 | |
| 162 | CLXX.IP.Odontologia Hospitalizado                | |
| 226 | CLXX.OT.Medico Cirujano Serv. Quirurgicos        | |
| 228 | CLXX.EM.Medico Urgencia                          | |
| 282 | CLXX.EM.Medico Urgencia G-O                      | |
| 19  | CLXX.EM.Medico Urgencia ESI                      | |
| 69  | CLXX.IP.Profesionales Clinicos Hospitalizado     | |

## UI TrakCare - Componentes

### Worklist de Interconsultas

- **Componente**: `Region.CLXX.Model.EPVisitNumber.ClinicWorkList.LTInterconsultasInternas`
- **Menu padre**: "Solicitudes Clinicas" (tooltip: "Solicitudes de Interconsultas")
- **Sub-menus**:
  - "Lista IC internas" (`CLXX.Internal Consult Worklist`)
  - "Interconsultas Sin Asignar" (`CLXX.ICInternasSol`)
  - "Interconsultas Asignadas" (`CLXX.ICInternasAsig`)
- **Columnas visibles**: Fecha Inicio, Hora Inicio, Registro IC, Nombre de la Orden,
  Nombre, RUN, Sexo, Fecha Nacimiento, Habitacion, Servicio, Solicitado,
  Estado de Orden, Prioridad, Usuario Ultima Actualizacion

### Formulario "Datos de Contacto"

- Se abre al hacer clic en una IC de la worklist
- Incluye banner del paciente (`Region.CLXX.Model.PAPerson.Banner`)
- Campos obligatorios (*): Fecha, Hora, Estatus de la Solicitud, Metodo de contacto, Duracion
- Campos informativos: Item de Orden, Establecimiento, Local, Profesional de la Salud

## Tablas Investigadas (descartadas)

| Tabla | Resultado |
|-------|-----------|
| `OE_OrdItem.OEORI_ConsCateg_DR` | NULL para todos los HOVA* |
| `OE_OrdItem.OEORI_Consult_DR` | NULL para todos los HOVA* |
| `OE_OrdItem.OEORI_Questionnaire` | NULL para todos los HOVA* |
| `ARC_ItmMast.ARCIM_Questionnaire_DR` | NULL para todos los HOVA* |
| `ARC_ItmMast.ARCIM_UserDefWindow_DR` | NULL para todos los HOVA* |
| `Region_CLXX_Misc_User.OEOrdItem.COEORI_QuestID` | NULL en 94,020/94,020 registros |
| `PA_Consultation` | Tabla vacia (0 registros) |
| `PA_ConsultationLink` | Tabla vacia (0 registros) |
| `OE_OrdExec` para HOVA* | 0 registros de ejecucion |
| `epr.TaskList` para HOVA* | No vinculado a interconsultas |
| `OEC_ConsultCateg` templates SOAP | Solo 9 categorias con templates, ninguna IC |

## Tablas de Configuracion (OEC_ConsultCateg*)

Existen pero NO se usan para interconsultas HOVA*:
- `OEC_ConsultCateg` — 378 categorias, pero sin link a HOVA*
- `OEC_ConsultCategQuestion` — questionnaires por categoria (QUES_UserDefWindow_DR)
- `OEC_ConsultCategFollowOrd` — ordenes de seguimiento (FOL_ARCIM_DR)
- `OEC_ConsultCategConsActions` — acciones SOAP
- `OEC_ConsultCategGroups` — grupos por categoria

## Conclusion

El flujo completo de una interconsulta interna es:

1. **Orden**: Medico solicitante crea OE_OrdItem con item HOVA*
2. **Ruteo**: `ITM2_Group_DR` en OE_OrdItem2 determina el grupo receptor
3. **Estado inicial**: OE_OrdStatus registra Status 5 "Inactivo" y luego 12 "Solicitado"
4. **Worklist**: La orden "Solicitada" aparece en "IC internas no asignadas"
5. **Asignacion**: El medico interconsultor abre la IC y llena el formulario "Datos de Contacto"
   que se almacena en **PA_EnquiryContact** (ENQ_OEOrdItem_DR vincula la orden)
6. **Registro contacto**: Se registra estatus (Asignada/En Proceso/Finalizada),
   metodo (WhatsApp/Telefonico/Correo), duracion en minutos
7. **Ejecutado**: OE_OrdStatus transita a Status 3 "Ejecutado"
8. **Respuesta clinica**: El medico crea un MR_Encounter con la nota clinica

## Preguntas Resueltas

1. **Como se marca una IC como "respondida"?**
   → Via OE_OrdStatus: Status 12 "Solicitado" -> Status 3 "Ejecutado"
2. **Que formulario usa el medico interconsultor?**
   → "Datos de Contacto" almacenado en PA_EnquiryContact
3. **Que metodos de contacto existen?**
   → WhatsApp, Telefonico, Correo Electronico (PAC_ContMethod)

## Preguntas Abiertas

1. El encuentro MR_Encounter se vincula directamente a la orden HOVA* o solo al episodio?
2. Existe un mecanismo de notificacion automatica cuando la IC es respondida?
3. La transicion de "Solicitado" a "Ejecutado" es manual o automatica al guardar PA_EnquiryContact?

---

Investigacion: 2026-02-26 | Fuente: ALMA LIVE-CLOV | Actualizado: sesion 2
