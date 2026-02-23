# lab.CF_Medtrak_Labtrak

**Schema:** lab
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFML_RowID | bigint | PK |  | NO | - |
| CFML_DOC_Company_DR | varchar |  | FK | SI | DOC Company DR |
| CFML_DOC_Copies | numeric |  |  | SI | DOC Number of Copies |
| CFML_DOC_CourierRun_DR | varchar |  | FK | SI | DOC Courier Run DR |
| CFML_DOC_PaymentCode_DR | varchar |  | FK | SI | DOC Payment Code DR |
| CFML_DOC_PrintFormat_DR | varchar |  | FK | SI | DOC Print Format DR |
| CFML_DOC_Priority_DR | varchar |  | FK | SI | DOC Priority DR |
| CFML_Doctor_DR | varchar |  | FK | SI | Default Doctor Code |
| CFML_MedtrakNamespace | varchar |  |  | SI | Medtrak Namespace |
| CFML_MedtrakURL | varchar |  |  | SI | Medtrak URL |
| CFML_PAT_CollectedBy_DR | varchar |  | FK | SI | PAT Collected By DR |
| CFML_PAT_EntrySpecimen | varchar |  |  | SI | Pat Entry - Specimen priority 1 Only |
| CFML_PAT_Fsting_DR | varchar |  | FK | SI | PAT Fsting DR |
| CFML_PAT_InitiationCode_DR | varchar |  | FK | SI | PAT Initiation Code DR |
| CFML_PAT_PaymentCode_DR | varchar |  | FK | SI | PAT Payment Code DR |
| CFML_PAT_Priority_DR | varchar |  | FK | SI | PAT Priority DR |
| CFML_PAT_UserID_DR | varchar |  | FK | SI | PAT User ID DR |
| CFML_TestSetCancelReason_DR | varchar |  | FK | SI | Test Set cancel Reason |
| CFML_TestSetReason_DR | varchar |  | FK | SI | Test Set Reason |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*