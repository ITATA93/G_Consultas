# SQLUser.PA_Dentist

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DENT_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| ChildQ74DR | - |  |  | SI | Child Reference: Pain Assessment |
| DENT_Childsub | double |  |  | NO | Childsub |
| DENT_DateFrom | date |  |  | SI | Date From |
| DENT_DateTo | date |  |  | SI | Date To |
| DENT_RefDocClinic_DR | varchar |  | FK | SI | Des Ref RefDocClinic |
| DENT_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| DENT_RowId | varchar |  |  | NO | - |
| DENT_UpdateDate | date |  |  | SI | Update Date |
| DENT_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| DENT_UpdateTime | time |  |  | SI | Update Time |
| DENT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q73Q1 | - |  |  | SI | Date |
| Q73Q2 | - |  |  | SI | Wound edge / margin |
| Q73Q3 | - |  |  | SI | Wound edge comments |
| Q73Q4 | - |  |  | SI | Periwound |
| Q73Q5 | - |  |  | SI | Periwound comments |
| Q73Q6 | - |  |  | SI | Entered by |
| Q73Q7 | - |  |  | SI | Wound edge / margin |
| Q73Q8 | - |  |  | SI | Periwound |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*