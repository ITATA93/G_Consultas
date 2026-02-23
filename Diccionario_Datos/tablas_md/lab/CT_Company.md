# lab.CT_Company

**Schema:** lab
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCO_RowId | varchar | PK |  | NO | - |
| CTCO_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTCO_Address | varchar |  |  | SI | Address |
| CTCO_Address1 | varchar |  |  | SI | Address 1 |
| CTCO_Address2 | varchar |  |  | SI | Address 2 |
| CTCO_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTCO_Address4_State | varchar |  |  | SI | State_DR |
| CTCO_Address5_PostCode | varchar |  |  | SI | Post Code |
| CTCO_BankingCode_DR | varchar |  | FK | SI | Banking Code |
| CTCO_Code | varchar |  |  | NO | Code |
| CTCO_CurrentPathologist_DR | varchar |  | FK | SI | Current Pathologist DR |
| CTCO_CurrentProviderNumber | varchar |  |  | SI | Current Provider Number |
| CTCO_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTCO_Name | varchar |  |  | SI | Company Name |
| CTCO_Phone | varchar |  |  | SI | Phone |
| CTCO_RegistrationNumber | varchar |  |  | SI | Company Registration Number |
| CTCO_xxx3 | varchar |  |  | SI | Provider Change |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*