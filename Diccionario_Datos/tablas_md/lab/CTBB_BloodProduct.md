# lab.CTBB_BloodProduct

**Schema:** lab
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBP_RowID | varchar | PK |  | NO | - |
| BBBP_128_Codes | varchar |  |  | SI | 128 Codes |
| BBBP_ActiveFlag | varchar |  |  | SI | Active Flag |
| BBBP_AntiDVolume | double |  |  | SI | Anti-D Volume |
| BBBP_Autologous | varchar |  |  | SI | Autologous |
| BBBP_BarCode | varchar |  |  | SI | Bar Code |
| BBBP_BatchProduct | varchar |  |  | SI | Batch Product |
| BBBP_Code | varchar |  |  | NO | Code |
| BBBP_Comments | varchar |  |  | SI | Comments |
| BBBP_ConfirmBloodGroup | varchar |  |  | SI | Confirm Blood Group |
| BBBP_DefaultAntigen | varchar |  |  | SI | Default antigen values |
| BBBP_Description | varchar |  |  | SI | Description |
| BBBP_DisplaySequence | numeric |  |  | SI | Display Sequence |
| BBBP_Factor8Strength | varchar |  |  | SI | Factor VIII Strength |
| BBBP_FullDescription | varchar |  |  | SI | Full Description |
| BBBP_Hold | numeric |  |  | SI | Hours to hold after Issue |
| BBBP_IgnoreTags | varchar |  |  | SI | Ignore Tags |
| BBBP_IssueCheckGroup | varchar |  |  | SI | Issue Check Group |
| BBBP_Match_ABO_Rh | varchar |  |  | SI | Match ABO Rh |
| BBBP_MinsOutsideArea | numeric |  |  | SI | Mins outside area |
| BBBP_NormalLife | numeric |  |  | SI | Normal Life |
| BBBP_PackReceive_Location_DR | varchar |  | FK | SI | Pack Receive default Location DR |
| BBBP_PackReceive_Status_DR | varchar |  | FK | SI | Pack Receive default Status DR |
| BBBP_PackReceive_Transaction_DR | varchar |  | FK | SI | Pack Receive default Transaction DR |
| BBBP_PackSize | varchar |  |  | SI | Pack Size |
| BBBP_ProductGroup_DR | varchar |  | FK | SI | ProductGroup_DR |
| BBBP_RecordPackGroup | varchar |  |  | SI | Record Pack Group |
| BBBP_UseInDonorModule | varchar |  |  | SI | Use In Donor Module |
| BBBP_XMatchProduct | varchar |  |  | SI | XMatch Product |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*