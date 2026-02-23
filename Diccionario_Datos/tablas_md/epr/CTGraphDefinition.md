# epr.CTGraphDefinition

**Schema:** epr
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| GRPH1Height | integer |  |  | SI | Flowsheet Graph Height |
| GRPH2Height | integer |  |  | SI | Flowsheet Graph Height |
| GRPH3Height | integer |  |  | SI | Flowsheet Graph Height |
| GRPHAdHocGraph | varchar |  |  | SI | - |
| GRPHCode | varchar |  |  | NO | - |
| GRPHDateFrom | date |  |  | SI | Date From |
| GRPHDateFromCurrent | varchar |  |  | SI | - |
| GRPHDateFromDobOffset | integer |  |  | SI | - |
| GRPHDateFromOffset | varchar |  |  | SI | - |
| GRPHDateTo | date |  |  | SI | Date To |
| GRPHDateToCurrent | varchar |  |  | SI | - |
| GRPHDateToDobOffset | integer |  |  | SI | - |
| GRPHDateToOffset | varchar |  |  | SI | - |
| GRPHDesc | varchar |  |  | SI | - |
| GRPHDiagnosisGroup1 | varchar |  |  | SI | - |
| GRPHFirstObsItemDR | bigint |  | FK | SI | - |
| GRPHGraphEachItemSeparately | varchar |  |  | SI | - |
| GRPHGraphType | varchar |  |  | SI | - |
| GRPHHeight | varchar |  |  | SI | - |
| GRPHNoOfIntervals | integer |  |  | SI | Number of intervals for partogram |
| GRPHObsStatus | varchar |  |  | SI | Observation Item Status |
| GRPHOverlayMeds | varchar |  |  | SI | - |
| GRPHOverlayProcs | varchar |  |  | SI | - |
| GRPHPHCCat | varchar |  |  | SI | - |
| GRPHPHCCatSmartGraph | varchar |  |  | SI | - |
| GRPHPregnancyEvent | varchar |  |  | SI | Pregnancy Event Graph |
| GRPHShortDescription | varchar |  |  | SI | - |
| GRPHShowEWS | varchar |  |  | SI | - |
| GRPHShowEWSLoc | varchar |  |  | SI | Show Location Specific Early Warning Ranges |
| GRPHShowReferenceLine | varchar |  |  | SI | - |
| GRPHTimeFromOffset | varchar |  |  | SI | - |
| GRPHUserCreatedDR | bigint |  | FK | SI | Log 44734 - 30-09-2004 : New field to store User t... |
| GRPHUserGraph | varchar |  |  | SI | - |
| GRPHWidth | varchar |  |  | SI | - |
| GRPHXAxisIncrement | integer |  |  | SI | - |
| GRPHXAxisIncrementUnit | varchar |  |  | SI | - |
| GRPHXAxisIntervalType | varchar |  |  | SI | X Axis Label Units |
| GRPHY1AxisMax | varchar |  |  | SI | - |
| GRPHY1AxisMin | varchar |  |  | SI | - |
| GRPHY1AxisProfile | varchar |  |  | SI | - |
| GRPHY1AxisStep | varchar |  |  | SI | - |
| GRPHY1AxisType | varchar |  |  | SI | - |
| GRPHY2AxisMax | varchar |  |  | SI | - |
| GRPHY2AxisMin | varchar |  |  | SI | - |
| GRPHY2AxisProfile | varchar |  |  | SI | - |
| GRPHY2AxisStep | varchar |  |  | SI | - |
| GRPHY2AxisType | varchar |  |  | SI | - |
| GRPHY3AxisMax | varchar |  |  | SI | - |
| GRPHY3AxisMin | varchar |  |  | SI | - |
| GRPHY3AxisProfile | varchar |  |  | SI | - |
| GRPHY3AxisStep | varchar |  |  | SI | - |
| GRPHY3AxisType | varchar |  |  | SI | - |
| GRPHY4AxisMax | varchar |  |  | SI | - |
| GRPHY4AxisMin | varchar |  |  | SI | - |
| GRPHY4AxisProfile | varchar |  |  | SI | - |
| GRPHY4AxisStep | varchar |  |  | SI | - |
| GRPHY4AxisType | varchar |  |  | SI | - |
| GRPHY5AxisMax | varchar |  |  | SI | - |
| GRPHY5AxisMin | varchar |  |  | SI | - |
| GRPHY5AxisProfile | varchar |  |  | SI | - |
| GRPHY5AxisStep | varchar |  |  | SI | - |
| GRPHY5AxisType | varchar |  |  | SI | - |
| GRPHY6AxisMax | varchar |  |  | SI | - |
| GRPHY6AxisMin | varchar |  |  | SI | - |
| GRPHY6AxisProfile | varchar |  |  | SI | - |
| GRPHY6AxisStep | varchar |  |  | SI | - |
| GRPHY6AxisType | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*