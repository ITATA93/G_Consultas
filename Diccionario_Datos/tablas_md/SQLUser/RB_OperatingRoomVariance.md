# SQLUser.RB_OperatingRoomVariance

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VAR_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| VAR_AnaStartTimeReasText | varchar |  |  | SI | Variance Reason Free Text for period from the Arri... |
| VAR_AnaStartTimeReas_DR | bigint |  | FK | SI | Variance Reason for period from the Arrival in the... |
| VAR_AnaTimeReasText | varchar |  |  | SI | Variance Free Text Reason for Anaesthetic Time vs ... |
| VAR_AnaTimeReas_DR | bigint |  | FK | SI | Variance Reason for Anaesthetic Time vs planned in... |
| VAR_AreaOutTimeReasText | varchar |  |  | SI | Variance Reason Free Text for period from the Reco... |
| VAR_AreaOutTimeReas_DR | bigint |  | FK | SI | Variance Reason for period from the Recovery Ready... |
| VAR_Childsub | double |  |  | NO | Childsub |
| VAR_CleanUpTimeReasText | varchar |  |  | SI | Variance Reason Free Text for Clean Up Time vs pla... |
| VAR_CleanUpTimeReas_DR | bigint |  | FK | SI | Variance Reason for Clean Up Time against planned ... |
| VAR_InAnaRoomTimeReasText | varchar |  |  | SI | Variance Reason Free Text for period from the Pati... |
| VAR_InAnaRoomTimeReas_DR | bigint |  | FK | SI | Variance for period from the Patient Arrival in Th... |
| VAR_IntoTheatreRoomTimeReasText | varchar |  |  | SI | Variance Reason Free Text for period from the Area... |
| VAR_IntoTheatreRoomTimeReas_DR | bigint |  | FK | SI | Variance for period from the Area In Date/Time and... |
| VAR_ORAnaesthesia_DR | varchar |  | FK | SI | des ref to OR_Anaesthesia |
| VAR_OTArrivalTimeReasText | varchar |  |  | SI | Variance Reason Free Text for period from the ackn... |
| VAR_OTArrivalTimeReas_DR | bigint |  | FK | SI | Variance Reason for period from the acknowledgemen... |
| VAR_OutTheatreTimeReasText | varchar |  |  | SI |  Variance Reason Free Text for period from the Ope... |
| VAR_OutTheatreTimeReas_DR | bigint |  | FK | SI |  Variance Reason for period from the Operation End... |
| VAR_PreSetupTimeReasText | varchar |  |  | SI | Variance Reason Free Text for Setup Time vs planne... |
| VAR_PreSetupTimeReas_DR | bigint |  | FK | SI | Variance Reason for Setup Time vs planned in OT Bo... |
| VAR_RecoveryInTheatreOutReasText | varchar |  |  | SI | Variance Reason Free Text for period from the Reco... |
| VAR_RecoveryInTheatreOutReas_DR | bigint |  | FK | SI | Variance for period from the Patient Arrival in Th... |
| VAR_RecoveryTimeReasText | varchar |  |  | SI |  Variance Reason Free Text for period from the Arr... |
| VAR_RecoveryTimeReas_DR | bigint |  | FK | SI |  Variance Reason for period from the Arrival in th... |
| VAR_RowId | varchar |  |  | NO | - |
| VAR_SurgTimeReasText | varchar |  |  | SI | Variance Reason Free Text for the Surgical Time vs... |
| VAR_SurgTimeReas_DR | bigint |  | FK | SI | Variance Reason for the Surgical Time vs planned i... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*