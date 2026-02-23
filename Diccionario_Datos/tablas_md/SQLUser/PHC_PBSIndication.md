# SQLUser.PHC_PBSIndication

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBSIND_RowId | bigint | PK |  | NO | - |
| PBSIND_Category_DR | bigint |  | FK | SI | DEPRECATED]Deprecated in TrakCare T2018+ as of TC-... |
| PBSIND_Code | varchar |  |  | NO | Code |
| PBSIND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBSIND_Condition_DR | bigint |  | FK | SI | PBS Condition |
| PBSIND_DateFrom | date |  |  | SI | Date From |
| PBSIND_DateTo | date |  |  | SI | Date To |
| PBSIND_Desc | varchar |  |  | NO | Description |
| PBSIND_Episodicity_DR | bigint |  | FK | SI | PBS Episodicity |
| PBSIND_Note | varchar |  |  | SI | DEPRECATED]Deprecated in TrakCare T2018+ as of TC-... |
| PBSIND_Owner | varchar |  |  | SI | Owner |
| PBSIND_Severity_DR | bigint |  | FK | SI | PBS Severity |
| PBSIND_StreamlineCode | integer |  |  | SI | DEPRECATED]Deprecated in TrakCare T2018+ as of TC-... |
| PBSIND_Text | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2018+ as of TC... |
| PBSIND_UpdatedDate | date |  |  | SI | Updated Date |
| PBSIND_UpdatedTime | time |  |  | SI | Updated Time |
| PBSIND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*