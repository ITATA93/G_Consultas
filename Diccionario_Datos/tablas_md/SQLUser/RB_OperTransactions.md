# SQLUser.RB_OperTransactions

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANS_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| TRANS_Childsub | double |  |  | NO | Childsub |
| TRANS_Date | date |  |  | SI | Date |
| TRANS_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| TRANS_OriginalDate | date |  |  | SI | Original Date |
| TRANS_OriginalTime | time |  |  | SI | Original Time |
| TRANS_ReasonForChange | varchar |  |  | SI | Reason For Change |
| TRANS_ReasonForOTBookChange_DR | bigint |  | FK | SI | Reason for Booked OT change |
| TRANS_RowId | varchar |  |  | NO | - |
| TRANS_Time | time |  |  | SI | Time |
| TRANS_UpdateDate | date |  |  | SI | Update Date |
| TRANS_UpdateTime | time |  |  | SI | Update Time |
| TRANS_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*