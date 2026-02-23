# SQLUser.LBDR_Recipient

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRR_ParRef | bigint | PK |  | NO | Parent Reference LBDRBatch DR |
| ChildQ80DR | - |  |  | SI | Child Reference: Actitud |
| LBDRR_Clinic_DR | bigint |  | FK | SI | Clinic for Referring Doctor
It's blank when the r... |
| LBDRR_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| LBDRR_CumulativeOrder | varchar |  |  | SI | The recipient's choice of Episode Sequence in Cumu... |
| LBDRR_CumulativePreference | varchar |  |  | SI | The recipient's strategy for cumulatives
Y = prin... |
| LBDRR_DoctorsReportsType | varchar |  |  | SI | Report Type
The ReportType to use for Doctors Rep... |
| LBDRR_LanguageID | varchar |  |  | SI | Recipient Language
The ID of the language (User.S... |
| LBDRR_RecipientAddress | varchar |  |  | SI | Recipient Address
The Address of the Recipient as... |
| LBDRR_RecipientAddressCity | varchar |  |  | SI | Recipient Address City
The City of the Recipient... |
| LBDRR_RecipientAddressState | varchar |  |  | SI | Recipient Address State
The State of the Recipien... |
| LBDRR_RecipientAddressStreet | varchar |  |  | SI | Recipient Address Street
The Street Address of th... |
| LBDRR_RecipientAddressZip | varchar |  |  | SI | Recipient Address Zip
The Zipcode of the Recipien... |
| LBDRR_RecipientCode | varchar |  |  | SI | The Code of the Recipient (For Readability) |
| LBDRR_RecipientDesc | varchar |  |  | SI | Recipient
The Name (Desc) of the Recipient
For a... |
| LBDRR_RecipientFooterClass | varchar |  |  | SI | Recipient Footer Zen Report - a copy of LBCDRRecip... |
| LBDRR_RecipientHeaderClass | varchar |  |  | SI | Recipient Header Zen Report - a copy of LBCDRRecip... |
| LBDRR_RecipientID | varchar |  |  | SI | The Recipient (ID of User.CTCareProv, User.CTLoc, ... |
| LBDRR_RecipientPhone | varchar |  |  | SI | Recipient Phone
The Phone number of the Recipient... |
| LBDRR_RecipientSortKey | varchar |  |  | SI | The Sortkey used to sort recipient type and recipi... |
| LBDRR_RecipientType | varchar |  |  | SI | Recipient Type
The type of recipient (C, L, R, or... |
| LBDRR_ReportMode | varchar |  |  | SI | Report Mode
Printed, Electronic. |
| LBDRR_RowID | varchar |  |  | NO | - |
| Q79Q1 | - |  |  | SI | Características |
| Q79Q2 | - |  |  | SI | Evaluación |
| Q79Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*