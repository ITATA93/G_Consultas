# SQLUser.OE_AdmixManufUnit

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UNIT_ParRef | varchar | PK |  | NO | OE_AdmixManuf Parent Reference |
| ChildQ08DR | - |  |  | SI | Child Reference: Pain Assessment |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Pain prevention |
| Q06Q4 | - |  |  | SI | Care |
| Q06Q5 | - |  |  | SI | Type of dressing |
| Q06Q6 | - |  |  | SI | Note |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| UNIT_Childsub | double |  |  | NO | Childsub |
| UNIT_ConditionalPass | varchar |  |  | SI | Conditional Pass  |
| UNIT_Fail | varchar |  |  | SI | Fail   |
| UNIT_Pass | varchar |  |  | SI | Pass  |
| UNIT_RowId | varchar |  |  | NO | - |
| UNIT_UnitNumber | integer |  |  | SI | Unit Number  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*