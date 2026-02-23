# SQLUser.PA_WaitingListReview

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REV_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| REV_Childsub | double |  |  | NO | Childsub |
| REV_Comment | varchar |  |  | SI | Comment |
| REV_Date | date |  |  | SI | Date |
| REV_DateLetterPrinted | date |  |  | SI | Date Letter Printed |
| REV_EffDate | date |  |  | SI | Effective Date |
| REV_LetterSentTo | varchar |  |  | SI | Letter Sent To |
| REV_LetterType_DR | bigint |  | FK | SI | Des Ref LetterType |
| REV_PatientRespond | varchar |  |  | SI | Patient Respond |
| REV_PatientResponseDate | date |  |  | SI | PatientResponseDate |
| REV_RespondentDR | bigint |  | FK | SI | Respondent |
| REV_ResponseDueDate | date |  |  | SI | ResponseDueDate |
| REV_RevOutcome_DR | bigint |  | FK | SI | Des Ref RevOutcome |
| REV_RevStatus_DR | bigint |  | FK | SI | Des Ref RevStatus |
| REV_ReviewDate | date |  |  | SI | ReviewDate |
| REV_RowId | varchar |  |  | NO | - |
| REV_Time | time |  |  | SI | Time |
| REV_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| REV_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*