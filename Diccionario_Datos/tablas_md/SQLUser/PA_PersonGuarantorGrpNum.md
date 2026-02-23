# SQLUser.PA_PersonGuarantorGrpNum

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GUA_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| GUA_Childsub | double |  |  | NO | Childsub |
| GUA_CustomerID | varchar |  |  | SI | Customer ID |
| GUA_CustomerType | varchar |  |  | SI | Customer Type |
| GUA_DateFrom | date |  |  | SI | Date From |
| GUA_DateTo | date |  |  | SI | Date To |
| GUA_GuarantorGroup_DR | bigint |  | FK | SI | Des Ref ARCGuarantorGroup |
| GUA_GuarantorGrpNum | varchar |  |  | SI | Guarantor Group Number |
| GUA_RowId | varchar |  |  | NO | - |
| GUA_UpdateDate | date |  |  | SI | Last Update Date |
| GUA_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital - Des Ref CTHospital |
| GUA_UpdateMode | varchar |  |  | SI | Update Mode |
| GUA_UpdateTime | time |  |  | SI | Last Update Time |
| GUA_UpdateUser_DR | bigint |  | FK | SI | Last Update User - Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*