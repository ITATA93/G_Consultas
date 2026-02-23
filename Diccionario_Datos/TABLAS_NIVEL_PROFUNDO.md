# Tablas de Nivel Profundo ALMA (Nivel 3+)

Este documento complementa el diccionario con las tablas de niveles más profundos y sus relaciones jerárquicas.

## Resumen de Tablas por Dominio (SQLUser)

| Prefijo | Dominio | Tablas | Nivel | Descripción |
|---------|---------|--------|-------|-------------|
| **PA_** | Pacientes | 347 | 1-3 | Demografía, Admisiones |
| **MR_** | Registro Médico | 74 | 2-5 | Diagnósticos, Observaciones, Notas |
| **OE_** | Órdenes | 92 | 2-3 | Solicitudes, Items de orden |
| **LB_** | Laboratorio | 100 | 3-5 | Resultados, Muestras, QC |
| **OR_** | Pabellón | 63 | 3-5 | Cirugías, Anestesia |
| **PHC_** | Farmacia | 109 | 2-4 | Medicamentos, Interacciones |
| **RB_** | Resource Booking | 85 | 3-4 | Agenda, Recursos |
| **CT_** | Configuración | 204 | 1 | Maestros, Códigos |
| **ARC_** | Facturación | 291 | 2-4 | Tarifas, Billing |

---

## 1. Dominio Laboratorio (LB_) - Nivel 3+

### Jerarquía de Tablas
```
OE_OrdItem (Nivel 2)
└── LB_Episode (Nivel 3) - Episodio de laboratorio
    ├── LB_EpisodeGroup (Nivel 4)
    │   ├── LB_EpisodeGroupTestSet (Nivel 5)
    │   └── LB_EpisodeGroupSpecimenContainer (Nivel 5)
    ├── LB_Request (Nivel 4) - Solicitud de examen
    │   ├── LB_RequestTestSet (Nivel 5)
    │   └── LB_RequestSpecimenContainer (Nivel 5)
    └── LB_SpecimenContainer (Nivel 4) - Contenedor de muestra
        ├── LB_SpecimenContainerDetail (Nivel 5)
        └── LB_SpecimenContainerComment (Nivel 5)
```

### Tablas de Resultados (Nivel 4-5)
```
LB_TestSet (Nivel 4)
└── LB_TestSetItem (Nivel 5) - Ítem individual del test
    ├── LB_TestSetItemResult - Resultado
    ├── LB_TestSetItemAntibiotic - Antibiograma
    └── LB_TestSetItemInterpretation - Interpretación
```

### Tablas Principales LB_

| Tabla | Descripción |
|-------|-------------|
| `LB_Episode` | Episodio de laboratorio |
| `LB_TestSet` | Set de pruebas/exámenes |
| `LB_TestSetItem` | Ítem individual del test |
| `LB_TestSetItemResult` | Resultado del ítem |
| `LB_SpecimenContainer` | Contenedor de muestra |
| `LB_BloodProduct` | Productos sanguíneos |
| `LB_QCBatch` | Control de calidad |
| `LB_Worksheet` | Hojas de trabajo |

---

## 2. Dominio Pabellón/Quirófano (OR_) - Nivel 3+

### Jerarquía de Tablas
```
PA_Adm (Nivel 1)
└── OR_Anaesthesia (Nivel 3) - Registro anestésico
    ├── OR_Anaest_Operation (Nivel 4) - Operación
    │   ├── OR_An_Oper_Diagnosis (Nivel 5) - Diagnóstico quirúrgico
    │   ├── OR_An_Oper_SecondaryProc (Nivel 5) - Procedimientos secundarios
    │   ├── OR_An_Oper_Assistant (Nivel 5) - Asistentes
    │   ├── OR_An_Oper_Scrub_Nurse (Nivel 5) - Enfermera instrumentista
    │   └── OR_An_Oper_Circul_Nurse (Nivel 5) - Enfermera circulante
    ├── OR_AnaestLine (Nivel 4) - Líneas/Catéteres
    ├── OR_AnaestMonitorDevice (Nivel 4) - Dispositivos de monitoreo
    └── OR_AnaestComplications (Nivel 4) - Complicaciones
```

### Pathway Quirúrgico (OR_AnaestSurgPathway)
```
OR_AnaestSurgPathway (Nivel 4)
├── OR_AnaestSurgPathwayPatPosit - Posición paciente
├── OR_AnaestSurgPathwaySkinPrep - Preparación piel
├── OR_AnaestSurgPathwayDrainTube - Drenajes
├── OR_AnaestSurgPathwayDressing - Vendajes
├── OR_AnaestSurgPathwayEquip - Equipamiento
├── OR_AnaestSurgPathwaySterBatch - Esterilización
└── OR_AnaestSurgPathwayUrinaryCatheter - Catéter urinario
```

### Tablas Principales OR_

| Tabla | Descripción |
|-------|-------------|
| `OR_Anaesthesia` | Registro anestésico principal |
| `OR_Anaest_Operation` | Operación/Procedimiento |
| `OR_AnaestSurgPathway` | Pathway quirúrgico |
| `OR_PreanaestheticConsult` | Consulta preanestésica |
| `OR_AnaesTemplate` | Plantillas anestésicas |

---

## 3. Dominio Registro Médico (MR_) - Nivel 2-5

### Jerarquía de Tablas
```
PA_Adm (Nivel 1)
└── MR_Adm (Nivel 2) - Admisión de registro médico
    ├── MR_Diagnos (Nivel 3) - Diagnósticos
    │   ├── MR_DiagnosLymphInvasion (Nivel 4)
    │   └── MR_DiagnosDistalMetasta (Nivel 4)
    ├── MR_Observations (Nivel 3) - Signos vitales
    │   ├── MR_ObservationsAttribute (Nivel 4)
    │   └── MR_ObservationsAudit (Nivel 4)
    ├── MR_Allergy (Nivel 3) - Alergias
    ├── MR_Medication (Nivel 3) - Medicamentos actuales
    ├── MR_Procedures (Nivel 3) - Procedimientos
    ├── MR_Prescriptions (Nivel 3) - Prescripciones
    ├── MR_NursingNotes (Nivel 3) - Notas enfermería
    ├── MR_Evolution (Nivel 3) - Evoluciones
    └── MR_Encounter (Nivel 3) - Encuentros
        └── MR_EncEntry (Nivel 4)
            └── MR_EncEntryItem (Nivel 5)
```

### Tablas Principales MR_

| Tabla | Nivel | Descripción |
|-------|-------|-------------|
| `MR_Adm` | 2 | Registro médico de admisión |
| `MR_Diagnos` | 3 | Diagnósticos CIE-10 |
| `MR_Procedures` | 3 | Procedimientos realizados |
| `MR_Observations` | 3 | Signos vitales |
| `MR_Allergy` | 3 | Registro de alergias |
| `MR_Prescriptions` | 3 | Prescripciones médicas |
| `MR_CareEvent` | 3 | Eventos de cuidado |
| `MR_Encounter` | 3 | Encuentros clínicos |
| `MR_EncEntry` | 4 | Entradas de encuentro |
| `MR_EncEntryItem` | 5 | Ítems de entrada |

---

## 4. Dominio Farmacia (PHC_) - Nivel 2-4

### Jerarquía de Tablas
```
PHC_DrgMast (Nivel 2) - Maestro de medicamentos
├── PHC_DrgForm (Nivel 3) - Forma farmacéutica
│   ├── PHC_DrgFormPack (Nivel 4) - Presentaciones
│   ├── PHC_DrgFormAdminRoute (Nivel 4) - Vías de administración
│   └── PHC_DrgFormDefDose (Nivel 4) - Dosis por defecto
├── PHC_Generic (Nivel 3) - Genéricos
│   ├── PHC_GenericIngr (Nivel 4) - Ingredientes
│   ├── PHC_GenericInter (Nivel 4) - Interacciones
│   └── PHC_GenericDoseRange (Nivel 4) - Rangos de dosis
└── PHC_DrgInteraction (Nivel 3) - Interacciones
```

### Tablas Principales PHC_

| Tabla | Descripción |
|-------|-------------|
| `PHC_DrgMast` | Maestro de drogas/medicamentos |
| `PHC_Generic` | Nombres genéricos |
| `PHC_DrgForm` | Formas farmacéuticas |
| `PHC_AdministrationRoute` | Vías de administración |
| `PHC_Freq` | Frecuencias de administración |
| `PHC_AllergyGroup` | Grupos de alergia |
| `PHC_DrugInteractSeverity` | Severidad interacciones |

---

## 5. Navegación por Niveles

### Nivel 1 (Raíz)
- `PA_Person` - Persona física
- `PA_PatMas` - Paciente maestro

### Nivel 2 (Episodio)
- `PA_Adm` - Admisión/Episodio
- `MR_Adm` - Registro médico de admisión
- `OE_Order` - Cabecera de orden

### Nivel 3 (Transaccional)
- `OE_OrdItem` - Items de orden
- `MR_Diagnos` - Diagnósticos
- `MR_Observations` - Signos vitales
- `LB_Episode` - Episodio laboratorio
- `OR_Anaesthesia` - Registro anestésico

### Nivel 4+ (Detalle)
- `LB_TestSet` → `LB_TestSetItem` → `LB_TestSetItemResult`
- `OR_Anaest_Operation` → `OR_An_Oper_Diagnosis`
- `MR_EncEntry` → `MR_EncEntryItem`

---

## Consultas SQL de Ejemplo

### Resultados de Laboratorio (Nivel 5)
```sql
SELECT
    pe.PAPER_Name AS Paciente,
    lb.LBEPI_EpisodeNumber AS NumEpisodio,
    ts.LBTS_TestSetCode AS CodigoTest,
    tsi.LBTSI_TestItemCode AS ItemTest,
    tsir.Result AS Resultado,
    tsir.LBTSR_ResultDateTime AS FechaResultado
FROM SQLUser.LB_Episode lb
JOIN SQLUser.LB_TestSet ts ON ts.LBTS_LBEPI_ParRef = lb.LBEPI_RowId
JOIN SQLUser.LB_TestSetItem tsi ON tsi.LBTSI_LBTS_ParRef = ts.LBTS_RowId
JOIN SQLUser.LB_TestSetItemResult tsir ON tsir.LBTSR_LBTSI_ParRef = tsi.LBTSI_RowId
JOIN SQLUser.PA_PatMas pm ON lb.LBEPI_PAPMI_DR = pm.PAPMI_RowId
JOIN SQLUser.PA_Person pe ON pm.PAPMI_PAPER_DR = pe.PAPER_RowId
```

### Datos Quirúrgicos (Nivel 5)
```sql
SELECT
    an.ORAN_Date AS FechaCirugia,
    op.ORAOP_ProcedureDesc AS Procedimiento,
    diag.Diagnosis AS DiagnosticoQx,
    ass.ORAOA_Name AS Asistente
FROM SQLUser.OR_Anaesthesia an
JOIN SQLUser.OR_Anaest_Operation op ON op.ORAOP_ORAN_ParRef = an.ORAN_RowId
LEFT JOIN SQLUser.OR_An_Oper_Diagnosis diag ON diag.ParRef = op.ORAOP_RowId
LEFT JOIN SQLUser.OR_An_Oper_Assistant ass ON ass.ParRef = op.ORAOP_RowId
```

---

## Notas de Implementación

1. **Tablas _ParRef**: Indican relación padre-hijo (tabla hija)
2. **Tablas _DR**: Indican referencia a tabla maestra (FK)
3. **Tablas con sufijos largos**: Son sub-tablas de nivel 4-5
4. **Prefijos C (LBC_, PHC_, ORC_)**: Son tablas de configuración, no transaccionales
