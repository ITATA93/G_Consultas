# Region_CLXX_Misc_User.OEOrdItem

**Schema:** Region_CLXX_Misc_User
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| COEORI_CTPCP_DR | varchar |  | FK | SI | CTCareProv |
| COEORI_CarePrvTp_DR | bigint |  | FK | SI | CTCarPrvTp |
| COEORI_Date | date |  |  | SI | Date |
| COEORI_GES | integer |  |  | SI | GES - yes,no,maybe |
| COEORI_GESInfo | varchar |  |  | SI | GES - text information |
| COEORI_GESRST | bigint |  |  | SI | GES - Referral Stage Template |
| COEORI_GESRTST | bigint |  |  | SI | GES - Referral Template Stage Type |
| COEORI_GESSRQ | bigint |  |  | SI | GES - Source Ref Qualifier |
| COEORI_No | varchar |  |  | SI | Number |
| COEORI_OEORI_DR | varchar |  | FK | SI | Des Ref  |
| COEORI_PAAdm_DR | bigint |  | FK | SI | PAAdm |
| COEORI_QuestID | integer |  |  | SI | Questionnaire ID |
| COEORI_Repeated_DR | varchar |  | FK | SI | Daniel Natali INI
Create to save the original ite... |
| COEORI_Seq | integer |  |  | SI | Sequence |
| COEORI_Time | time |  |  | SI | Time |
| COEORI_Verified | integer |  |  | SI | Verified |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*