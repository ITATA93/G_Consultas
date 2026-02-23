# lab.CT_BillLocation

**Schema:** lab
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBL_RowID | varchar | PK |  | NO | - |
| CTBL_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTBL_Address | varchar |  |  | SI | Address |
| CTBL_Address1 | varchar |  |  | SI | Address 1 |
| CTBL_Address2 | varchar |  |  | SI | Address 2 |
| CTBL_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTBL_Address4_State_DR | varchar |  | FK | SI | State DR |
| CTBL_Address5_PostCode | varchar |  |  | SI | PostCode |
| CTBL_Code | varchar |  |  | NO | Code |
| CTBL_Comments | varchar |  |  | SI | Comments |
| CTBL_Contact | varchar |  |  | SI | Contact |
| CTBL_CurrentPathologist_DR | varchar |  | FK | SI | Current Pathologist DR |
| CTBL_CurrentProviderNumber | varchar |  |  | SI | Current Provider Number |
| CTBL_Description | varchar |  |  | SI | Description |
| CTBL_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTBL_Email | varchar |  |  | SI | Email |
| CTBL_Fax | varchar |  |  | SI | Fax |
| CTBL_FloppyFormat | varchar |  |  | SI | Floppy Format |
| CTBL_Language_DR | bigint |  | FK | SI | Language DR |
| CTBL_NumberOfCopies | varchar |  |  | SI | Number Of Copies |
| CTBL_Phone | varchar |  |  | SI | Phone |
| CTBL_ReferenceNumber | varchar |  |  | SI | Reference Number |
| CTBL_xxx | varchar |  |  | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*