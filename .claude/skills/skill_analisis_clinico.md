---
name: Análisis Clínico TrakCare
description: Skill para traducir lenguaje médico/clínico a estructuras técnicas de base de datos.
---

# Skill: Análisis Clínico

## 🏥 Objetivo
Actuar como "traductor" entre el personal de salud y la base de datos. Entender qué piden realmente cuando dicen "necesito la epicrisis" o "pacientes en cama".

## 📖 Diccionario Clínico-Técnico

| Concepto Clínico | Tabla(s) TrakCare | Filtros Clave / Campos |
|:---|:---|:---|
| **Ficha Clínica** | `PA_PatMas` | `PAPMI_No` |
| **Episodio / Ingreso** | `PA_Adm` | `PAADM_ADMNo` |
| **Rut Paciente** | `PA_Person` | `PAPER_ID` |
| **Diagnóstico (CIE10)**| `MR_Diagnos` | `MRDIA_DiagnosCode` (Join `MR_Adm`) |
| **Epicrisis (Alta)** | `PA_DischargeSummary` | Relacionado a `PA_Adm` |
| **Servicio / Sala** | `CT_Loc` | `CTLOC_Desc` |
| **Cama** | `PAC_Bed` | `BED_Code` |
| **Médico Tratante** | `CT_CareProv` | `CTPCP_Desc` |
| **Exámenes Lab** | `LB_Result` / `OE_Order` | Categ: `LAB` |
| **Recetas / Fármacos**| `OE_Order` | Categ: `PHARM` |

## 🧠 Lógica de Negocio Común

### "Pacientes Hospitalizados Actualmente" (Censo)
*   Tabla: `PA_Adm`
*   Condición 1: `PAADM_Type = 'I'` (Inpatient)
*   Condición 2: `PAADM_DischgDate IS NULL` (Sin fecha de alta)
*   Condición 3: `PAADM_VisitStatus != 'C'` (No cancelado)

### "Lista de Espera Quirúrgica"
*   Tabla: `WTL_WaitList` (o variantes según config local)
*   Estado: `Active`

### "Diagnósticos de Egreso"
*   Tabla: `MR_Diagnos`
*   Tipo: Buscar diagnósticos marcados como principales al alta, o simplemente todos los asociados al episodio `PA_Adm`.

## 🗣️ Interrogatorio Clínico (Prompting)
Cuando el usuario pida algo vago, pregunta:
1.  **¿Universo?**: ¿Todos los pacientes históricos o solo los actuales?
2.  **¿Granularidad?**: ¿Un resumen numérico o listado detalle por paciente?
3.  **¿Criterio de Fecha?**: ¿Fecha de ingreso, fecha de alta, fecha de orden médica?
