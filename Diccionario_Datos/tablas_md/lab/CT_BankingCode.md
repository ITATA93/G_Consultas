# lab.CT_BankingCode

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBA_RowId | varchar | PK |  | NO | - |
| CTBA_AccountNumber | varchar |  |  | SI | Account Number |
| CTBA_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTBA_Address | varchar |  |  | SI | Address |
| CTBA_Address1 | varchar |  |  | SI | Address 1 |
| CTBA_Address2 | varchar |  |  | SI | Address 2 |
| CTBA_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTBA_Address4_State | varchar |  |  | SI | State |
| CTBA_Address5_PostCode | varchar |  |  | SI | Post Code |
| CTBA_BSB_No | varchar |  |  | SI | BSB No |
| CTBA_Bank_DR | varchar |  | FK | SI | Bank |
| CTBA_Branch | varchar |  |  | SI | Branch |
| CTBA_Code | varchar |  |  | NO | Code |
| CTBA_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTBA_Fax | varchar |  |  | SI | Fax |
| CTBA_Phone | varchar |  |  | SI | Phone |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*