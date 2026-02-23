# SQLUser.PA_TrafficAccidentContact

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONT_ParRef | bigint | PK |  | NO | PA_TrafficAccident Parent Reference |
| CONT_Address1 | varchar |  |  | SI | Address1 |
| CONT_Address2 | varchar |  |  | SI | Address2 |
| CONT_Childsub | double |  |  | NO | Childsub |
| CONT_City_DR | bigint |  | FK | SI | Des Ref City |
| CONT_Comments | varchar |  |  | SI | Contact Comments |
| CONT_ContType_DR | bigint |  | FK | SI | Des Ref ContType |
| CONT_DateFrom | date |  |  | SI | Date From |
| CONT_DateTo | date |  |  | SI | Date To |
| CONT_Email | varchar |  |  | SI | Email |
| CONT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| CONT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| CONT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CONT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CONT_Name | varchar |  |  | SI | Name |
| CONT_Phone | varchar |  |  | SI | Phone |
| CONT_PrefContDay | varchar |  |  | SI | Preferred Contact Day |
| CONT_RowId | varchar |  |  | NO | - |
| CONT_Zip_DR | bigint |  | FK | SI | Des Ref Zip |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*