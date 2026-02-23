# SQLUser.PA_PersonEligibility

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ELG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ELG_AdmExpectedDate | date |  |  | SI | Approval Request Date |
| ELG_ApprovReqType | varchar |  |  | NO | Approval Request Type |
| ELG_Childsub | double |  |  | NO | Childsub |
| ELG_CreateDate | date |  |  | SI | Date Created |
| ELG_CreateUser_DR | bigint |  | FK | SI | User Created - Des Ref CreateUser |
| ELG_RowId | varchar |  |  | NO | - |
| ELG_UpdateDate | date |  |  | SI | Last Update Date |
| ELG_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital - Des Ref CTHospital |
| ELG_UpdateTime | time |  |  | SI | Last Update Time |
| ELG_UpdateUser_DR | bigint |  | FK | SI | Last Update User - Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*