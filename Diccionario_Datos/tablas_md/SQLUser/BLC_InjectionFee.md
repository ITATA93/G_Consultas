# SQLUser.BLC_InjectionFee

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INFEE_RowId | bigint | PK |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: METAS |
| INFEE_BillSubGr_DR | varchar |  | FK | SI | Des Ref BillSubGr |
| INFEE_CreatedDate | date |  |  | SI | Created Date |
| INFEE_CreatedTime | time |  |  | SI | Created Time |
| INFEE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INFEE_DateFrom | date |  |  | SI | Date From |
| INFEE_DateTo | date |  |  | SI | Date To |
| INFEE_InsType_DR | bigint |  | FK | SI | Des REf InsType_DR |
| INFEE_MaxNumberToPay | double |  |  | SI | MaxNumberToPay |
| INFEE_PatientType | varchar |  |  | SI | Patient Type |
| INFEE_UpdatedDate | date |  |  | SI | Updated Date |
| INFEE_UpdatedTime | time |  |  | SI | Updated Time |
| INFEE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q04Q1 | - |  |  | SI | Objetivos |
| Q04Q2 | - |  |  | SI | Estrategias o Actividades |
| Q04Q3 | - |  |  | SI | Responsables |
| Q04Q4 | - |  |  | SI | Plazo |
| Q04Q5 | - |  |  | SI | Indicador de Logro |
| Q04Q6 | - |  |  | SI | Cumplimiento |
| Q04Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*