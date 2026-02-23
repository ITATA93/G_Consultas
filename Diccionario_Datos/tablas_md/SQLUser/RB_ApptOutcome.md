# SQLUser.RB_ApptOutcome

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTC_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| OUTC_ApOutcome_DR | bigint |  | FK | SI | Des Ref Appt Outcome |
| OUTC_Childsub | double |  |  | NO | Childsub |
| OUTC_CommentHTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| OUTC_CommentHTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| OUTC_Date | date |  |  | SI | Date |
| OUTC_DateOfOutcome | date |  |  | SI | DateOfOutcome |
| OUTC_LastUpdateDate | date |  |  | SI | Last Update Date |
| OUTC_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| OUTC_LastUpdateTime | time |  |  | SI | Last Update Time |
| OUTC_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| OUTC_NewPAReferralPathway_DR | bigint |  | FK | SI | Link to the pathway that has been newly created fo... |
| OUTC_OrderItems | varchar |  |  | SI | OrderItems  |
| OUTC_PARefPathwayStage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |
| OUTC_Remarks | varchar |  |  | SI | Remarks |
| OUTC_RowId | varchar |  |  | NO | - |
| OUTC_Time | time |  |  | SI | Time |
| OUTC_User_DR | bigint |  | FK | SI | Des Ref User |
| OUTC_WaitingList_DR | bigint |  | FK | SI | Des Ref WaitingList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*