# SQLUser.BLC_OneOffCharge

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ONEOFF_RowId | bigint | PK |  | NO | - |
| ONEOFF_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ONEOFF_CreatedDate | date |  |  | SI | Created Date |
| ONEOFF_CreatedTime | time |  |  | SI | Created Time |
| ONEOFF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ONEOFF_DateFrom | date |  |  | SI | Date From |
| ONEOFF_DateTo | date |  |  | SI | Date To |
| ONEOFF_Name | varchar |  |  | SI | Name |
| ONEOFF_UpdatedDate | date |  |  | SI | Updated Date |
| ONEOFF_UpdatedTime | time |  |  | SI | Updated Time |
| ONEOFF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Frecuencia Cardiaca |
| Q02 | - |  |  | SI | Presión Arterial Sistólica |
| Q03 | - |  |  | SI | Presión Arterial Diastólica |
| Q04 | - |  |  | SI | % Saturación O2 |
| Q05 | - |  |  | SI | Síntomas |
| Q06 | - |  |  | SI | (mareo, debilidad, visión borrosa, síncope) |
| Q07 | - |  |  | SI | En decúbito supino |
| Q08 | - |  |  | SI | Frecuencia Cardiaca |
| Q08ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q09 | - |  |  | SI | Presión Arterial Sistólica |
| Q09ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q10 | - |  |  | SI | Presión Arterial Diastólica |
| Q10ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q11 | - |  |  | SI | Saturación O2 |
| Q11ObsDR | - |  |  | SI | Saturación O2 DR |
| Q12 | - |  |  | SI | Síntomas |
| Q13 | - |  |  | SI | 1er minuto en sedente borde cama |
| Q14 | - |  |  | SI | Frecuencia Cardiaca |
| Q14ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q15 | - |  |  | SI | Presión Arterial Sistólica |
| Q15ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q16 | - |  |  | SI | Presión Arterial Diastólica |
| Q16ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q17 | - |  |  | SI | Saturación O2 |
| Q17ObsDR | - |  |  | SI | Saturación O2 DR |
| Q18 | - |  |  | SI | Síntomas |
| Q19 | - |  |  | SI | 3er minuto en sedente borde cama |
| Q20 | - |  |  | SI | Frecuencia Cardiaca |
| Q20ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q21 | - |  |  | SI | Presión Arterial Sistólica |
| Q21ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q22 | - |  |  | SI | Presión Arterial Diastólica |
| Q22ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q23 | - |  |  | SI | Saturación O2 |
| Q23ObsDR | - |  |  | SI | Saturación O2 DR |
| Q24 | - |  |  | SI | Síntomas |
| Q25 | - |  |  | SI | 5to minuto en sedente borde cama |
| Q26 | - |  |  | SI | Frecuencia Cardiaca |
| Q26ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q27 | - |  |  | SI | Presión Arterial Sistólica |
| Q27ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q28 | - |  |  | SI | Presión Arterial Diastólica |
| Q28ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q29 | - |  |  | SI | Saturación O2 |
| Q29ObsDR | - |  |  | SI | Saturación O2 DR |
| Q30 | - |  |  | SI | Síntomas |
| Q31 | - |  |  | SI | 1er minuto en bípedo |
| Q32 | - |  |  | SI | Frecuencia Cardiaca |
| Q32ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q33 | - |  |  | SI | Presión Arterial Sistólica |
| Q33ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q34 | - |  |  | SI | Presión Arterial Diastólica |
| Q34ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q35 | - |  |  | SI | Saturación O2 |
| Q35ObsDR | - |  |  | SI | Saturación O2 DR |
| Q36 | - |  |  | SI | Síntomas |
| Q37 | - |  |  | SI | 3er minuto en bípedo |
| Q38 | - |  |  | SI | Frecuencia Cardiaca |
| Q38ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q39 | - |  |  | SI | Presión Arterial Sistólica |
| Q39ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q40 | - |  |  | SI | Presión Arterial Diastólica |
| Q40ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q41 | - |  |  | SI | Saturación O2 |
| Q41ObsDR | - |  |  | SI | Saturación O2 DR |
| Q42 | - |  |  | SI | Síntomas |
| Q43 | - |  |  | SI | 5to minuto en bípedo |
| Q44 | - |  |  | SI | Frecuencia Cardiaca |
| Q44ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q45 | - |  |  | SI | Presión Arterial Sistólica |
| Q45ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q46 | - |  |  | SI | Presión Arterial Diastólica |
| Q46ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q47 | - |  |  | SI | Saturación O2 |
| Q47ObsDR | - |  |  | SI | Saturación O2 DR |
| Q48 | - |  |  | SI | Síntomas |
| Q49 | - |  |  | SI | Evaluación de la prueba |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*