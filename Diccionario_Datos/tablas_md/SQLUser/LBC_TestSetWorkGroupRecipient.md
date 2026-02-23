# SQLUser.LBC_TestSetWorkGroupRecipient

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSWGR_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetWorkGroup DR |
| ChildQ70DR | - |  |  | SI | Child Reference: Extremidades |
| LBCTSWGR_CareProvider_DR | varchar |  | FK | SI | Doctor |
| LBCTSWGR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSWGR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSWGR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSWGR_Location_DR | bigint |  | FK | SI | Patient Location |
| LBCTSWGR_RecipientID | varchar |  |  | SI | Recipient ID
CareProvider, Location, ReferringDoc... |
| LBCTSWGR_RecipientType | varchar |  |  | NO | Recipient Type |
| LBCTSWGR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCTSWGR_ReportPage_DR | bigint |  | FK | SI | Report Page |
| LBCTSWGR_RowID | varchar |  |  | NO | - |
| LBCTSWGR_ThirdParty_DR | bigint |  | FK | SI | Third Party |
| Q05Q0 | - |  |  | SI | Lesión |
| Q05Q1 | - |  |  | SI | Localización |
| Q05Q2 | - |  |  | SI | Lateralidad |
| Q05Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*