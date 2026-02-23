# SQLUser.PHC_StreamlineIndication

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STMLIND_RowId | bigint | PK |  | NO | - |
| STMLIND_Code | varchar |  |  | NO | Code |
| STMLIND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STMLIND_CreatedDate | date |  |  | SI | Created Date |
| STMLIND_CreatedTime | time |  |  | SI | Created Time |
| STMLIND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STMLIND_DateFrom | date |  |  | SI | Date From |
| STMLIND_DateTo | date |  |  | SI | Date To |
| STMLIND_Desc | varchar |  |  | NO | Description |
| STMLIND_IndicationHTML | longvarchar |  |  | SI | IndicationHTML |
| STMLIND_Owner | varchar |  |  | SI | Owner |
| STMLIND_StreamlineNumber | varchar |  |  | SI | Streamline Number |
| STMLIND_UpdatedDate | date |  |  | SI | Updated Date |
| STMLIND_UpdatedTime | time |  |  | SI | Updated Time |
| STMLIND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*