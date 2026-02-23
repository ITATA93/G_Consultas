# SQLUser.OE_OrdSpecimen

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ23DR | - |  |  | SI | Child Reference: Deep Reflexes |
| Q22Q2 | - |  |  | SI | Reflex |
| Q22Q3 | - |  |  | SI | Left |
| Q22Q4 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SPEC_Childsub | double |  |  | NO | Childsub |
| SPEC_Code | varchar |  |  | SI | Code |
| SPEC_Container | varchar |  |  | SI | Container |
| SPEC_ContainerNumber | varchar |  |  | SI | Container Number |
| SPEC_Date | date |  |  | SI | Date |
| SPEC_DisplayFlag | varchar |  |  | SI | DisplayFlag |
| SPEC_Ext_RowID | varchar |  |  | SI | SPEC_Ext_RowID |
| SPEC_Processed | varchar |  |  | SI | Processed flag |
| SPEC_ReasonNotCollected | varchar |  |  | SI | ReasonNotCollected |
| SPEC_RowId | varchar |  |  | NO | - |
| SPEC_Time | time |  |  | SI | Time |
| SPEC_TubeFlag | varchar |  |  | SI | TubeFlag |
| SPEC_UpdateDate | date |  |  | SI | Update Date |
| SPEC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| SPEC_UpdateTime | time |  |  | SI | Update Time |
| SPEC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| SPEC_Vol_Collected | varchar |  |  | SI | Vol_Collected |
| SPEC_Vol_Required | varchar |  |  | SI | Vol_Required |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*