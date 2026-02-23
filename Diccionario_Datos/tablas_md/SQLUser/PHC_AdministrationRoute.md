# SQLUser.PHC_AdministrationRoute

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMR_RowId | bigint | PK |  | NO | - |
| ADMR_Code | varchar |  |  | NO | Code |
| ADMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMR_CodeTranslated | varchar |  |  | SI | Code Translated |
| ADMR_CreatedDate | date |  |  | SI | Created Date |
| ADMR_CreatedTime | time |  |  | SI | Created Time |
| ADMR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMR_DateFrom | date |  |  | SI | Date From |
| ADMR_DateTo | date |  |  | SI | Date To |
| ADMR_Desc | varchar |  |  | NO | Description |
| ADMR_DescTranslated | varchar |  |  | SI | Desc Translated |
| ADMR_EpiduralChart | varchar |  |  | SI | Epidural Chart |
| ADMR_IVType | varchar |  |  | SI | IVType |
| ADMR_MultiRoute | varchar |  |  | SI | Multi-Route |
| ADMR_OrderContext | varchar |  |  | SI | OrderContext |
| ADMR_Owner | varchar |  |  | SI | Owner |
| ADMR_RegAnestheticsPrograms | varchar |  |  | SI | Regional Anaesthetic Programs |
| ADMR_RouteSystem_DR | bigint |  | FK | SI | [DEPRECATED]Table PHC_RouteSystem has been depreca... |
| ADMR_ShortDesc | varchar |  |  | SI | Short Description  |
| ADMR_UpdatedDate | date |  |  | SI | Updated Date |
| ADMR_UpdatedTime | time |  |  | SI | Updated Time |
| ADMR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*