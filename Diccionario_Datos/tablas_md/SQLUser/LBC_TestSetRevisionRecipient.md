# SQLUser.LBC_TestSetRevisionRecipient

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRR_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevision DR |
| ChildQ30DR | - |  |  | SI | Child Reference: Orejas Alteradas |
| LBCTSRR_CareProvider_DR | varchar |  | FK | SI | Doctor |
| LBCTSRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRR_Courier_DR | bigint |  | FK | SI | Courier Run |
| LBCTSRR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRR_Location_DR | bigint |  | FK | SI | Patient Location |
| LBCTSRR_RecipientID | varchar |  |  | SI | Recipient ID
CareProvider, Location, ReferringDoc... |
| LBCTSRR_RecipientType | varchar |  |  | NO | Recipient Type
C = CareProvider
L = Location
R ... |
| LBCTSRR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCTSRR_ReportPage_DR | bigint |  | FK | SI | Report Page |
| LBCTSRR_RowID | varchar |  |  | NO | - |
| LBCTSRR_ThirdParty_DR | bigint |  | FK | SI | Third Party |
| Q18Q1 | - |  |  | SI | Localización |
| Q18Q2 | - |  |  | SI | Cuadrante |
| Q18Q3 | - |  |  | SI | Descripción |
| Q18Q4 | - |  |  | SI | Hemorragia Subconjuntival |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*