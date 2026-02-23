# SQLUser.PA_CancerRegLinkAdm

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADM_ParRef | bigint | PK |  | NO | PA_CancerReg Parent Reference |
| ADM_AdmCoding_DR | varchar |  | FK | SI | Des Ref AdmCoding |
| ADM_Appointment_DR | varchar |  | FK | SI | Des Ref Appointment |
| ADM_Childsub | double |  |  | NO | Childsub |
| ADM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ADM_OP_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ADM_RowId | varchar |  |  | NO | - |
| ADM_UpdateDate | date |  |  | SI | UpdateDate |
| ADM_UpdateTime | time |  |  | SI | UpdateTime |
| ADM_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| ADM_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Test |
| Q04 | - |  |  | SI | Left |
| Q05 | - |  |  | SI | Right |
| Q06 | - |  |  | SI | Bilateral Integration |
| Q07 | - |  |  | SI | Comments |
| Q08 | - |  |  | SI | Test |
| Q09 | - |  |  | SI | Left |
| Q10 | - |  |  | SI | Right |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | Rapid Alternating Movements (RAM) |
| Q13 | - |  |  | SI | Finger-to-nose |
| Q14 | - |  |  | SI | Finger-to-finger |
| Q15 | - |  |  | SI | Finger-to-therapist's finger |
| Q16 | - |  |  | SI | Alternate nose-to-finger |
| Q17 | - |  |  | SI | Mass grasp |
| Q18 | - |  |  | SI | Rebound phenomena |
| Q19 | - |  |  | SI | Rapid alternating movements - left |
| Q20 | - |  |  | SI | Rapid alternating movements - right |
| Q21 | - |  |  | SI | Rapid alternating movements - bilateral integratio... |
| Q22 | - |  |  | SI | Rapid alternating movements - comments |
| Q23 | - |  |  | SI | Finger-to-nose - left |
| Q24 | - |  |  | SI | Finger-to-nose - right |
| Q25 | - |  |  | SI | Finger-to-nose comments |
| Q26 | - |  |  | SI | Finger-to-finger - left |
| Q27 | - |  |  | SI | Finger-to-finger - right |
| Q28 | - |  |  | SI | Finger-to-finger comments |
| Q29 | - |  |  | SI | Finger-to-therapist's finger - left |
| Q30 | - |  |  | SI | Finger-to-therapist's finger - right |
| Q31 | - |  |  | SI | Finger-to-therapist's finger comments |
| Q32 | - |  |  | SI | Alternate nose-to-finger - left |
| Q33 | - |  |  | SI | Alternate nose-to-finger - right |
| Q34 | - |  |  | SI | Alternate nose-to-finger comments |
| Q35 | - |  |  | SI | Finger opposition - left |
| Q36 | - |  |  | SI | Finger opposition - right |
| Q37 | - |  |  | SI | Finger opposition comments |
| Q38 | - |  |  | SI | Mass grasp - left |
| Q39 | - |  |  | SI | Mass grasp - right |
| Q40 | - |  |  | SI | Mass grasp - bilateral integration |
| Q41 | - |  |  | SI | Mass grasp comments |
| Q42 | - |  |  | SI | Rebound phenomena - left |
| Q43 | - |  |  | SI | Rebound phenomena - right |
| Q44 | - |  |  | SI | Rebound phenomena - bilateral integration |
| Q45 | - |  |  | SI | Rebound phenomena comments |
| Q46 | - |  |  | SI | Additional detail |
| Q47 | - |  |  | SI | Assessment Instructions |
| Q48 | - |  |  | SI | Finger-to-Nose: |
| Q49 | - |  |  | SI | The shoulder is abducted to 90 degrees with elbow ... |
| Q50 | - |  |  | SI | Finger-to-Therapist’s finger: |
| Q51 | - |  |  | SI | The patient and therapist sit opposite each other.... |
| Q52 | - |  |  | SI | Finger-to-Finger: |
| Q53 | - |  |  | SI | Both shoulders are abducted to 90 degrees with the... |
| Q54 | - |  |  | SI | Alternate nose-to-finger: |
| Q55 | - |  |  | SI | The patient alternately touches the tip of his or ... |
| Q56 | - |  |  | SI | Finger Opposition: |
| Q57 | - |  |  | SI | The patient touches the tip of the thumb to the ti... |
| Q58 | - |  |  | SI | Mass Grasp: |
| Q59 | - |  |  | SI | An alteration is made between opening and closing ... |
| Q60 | - |  |  | SI | Rebound phenomena: |
| Q61 | - |  |  | SI | The patient is positioned with the elbow flexed. T... |
| Q62 | - |  |  | SI | Normally, the opposite muscle group (triceps) will... |
| Q63 | - |  |  | SI | Guide to assessment |
| Q64 | - |  |  | SI | No impairment: |
| Q65 | - |  |  | SI | Able to accomplish activity with no notable impair... |
| Q66 | - |  |  | SI | Impairment: |
| Q67 | - |  |  | SI | Activity completed or partially completed with imp... |
| Q68 | - |  |  | SI | Minimal impairment: |
| Q69 | - |  |  | SI | Able to accomplish activity, slightly less than no... |
| Q70 | - |  |  | SI | Moderate impairment: |
| Q71 | - |  |  | SI | Able to accomplish activity movements are slow, aw... |
| Q72 | - |  |  | SI | Severe impairment: |
| Q73 | - |  |  | SI | Able only to initiate activity without completion |
| Q74 | - |  |  | SI | Activity not possible: |
| Q75 | - |  |  | SI | Not tested: |
| Q76 | - |  |  | SI | Test not commenced - use comments to explain as re... |
| Q77 | - |  |  | SI | Finger opposition |
| Q78 | - |  |  | SI | Finger opposition - bilateral integration |
| Q79 | - |  |  | SI | Patient unable to initiate activity. |
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