# questionnaire.QTCPIPSAP

> Physiotherapy Inpatient Post Surgery Assessment and Plan

**Schema:** questionnaire
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy Inpatient Post Surgery Assessment and Plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Procedure |
| Q04 | varchar |  |  | SI | Procedure comment |
| Q05 | varchar |  |  | SI | Procedure side |
| Q06 | numeric |  |  | SI | Post operative day |
| Q07 | varchar |  |  | SI | Informed verbal consent for treatment |
| Q08 | varchar |  |  | SI | Treatment information handout provided |
| Q09 | varchar |  |  | SI | Treatment instructions |
| Q10 | varchar |  |  | SI | Subjective summary |
| Q11 | varchar |  |  | SI | Relevant social circumstances |
| Q12 | varchar |  |  | SI | Bed mobility |
| Q12ObsDR | varchar |  | FK | SI | Bed mobility DR |
| Q13 | varchar |  |  | SI | Bed mobility |
| Q13ObsDR | varchar |  | FK | SI | Bed mobility DR |
| Q14 | varchar |  |  | SI | Bed transfers |
| Q14ObsDR | varchar |  | FK | SI | Bed transfers DR |
| Q15 | varchar |  |  | SI | Mobility and transfers |
| Q15ObsDR | varchar |  | FK | SI | Mobility and transfers DR |
| Q16 | varchar |  |  | SI | Mobility and transfer comments |
| Q17 | varchar |  |  | SI | Femoral block in situ |
| Q18 | varchar |  |  | SI | Weight bearing comment |
| Q19 | varchar |  |  | SI | Mobility aid |
| Q19ObsDR | varchar |  | FK | SI | Mobility aid DR |
| Q20 | varchar |  |  | SI | Mobility aid comments |
| Q21 | varchar |  |  | SI | Gait |
| Q21ObsDR | varchar |  | FK | SI | Gait DR |
| Q22 | varchar |  |  | SI | Gait comment |
| Q23 | varchar |  |  | SI | Joint brace fitted |
| Q24 | varchar |  |  | SI | Brace instructions |
| Q25 | numeric |  |  | SI | Single distance walked |
| Q26 | varchar |  |  | SI | Meters |
| Q28 | varchar |  |  | SI | Sensation |
| Q29 | varchar |  |  | SI | Sensation comment |
| Q30 | varchar |  |  | SI | Co - contraction |
| Q31 | varchar |  |  | SI | Objective summary |
| Q32 | varchar |  |  | SI | Treatment |
| Q33 | varchar |  |  | SI | Exercises as per protocol |
| Q34 | varchar |  |  | SI | Exercise comment |
| Q35 | varchar |  |  | SI | Circumduction practiced |
| Q36 | varchar |  |  | SI | Circumduction comment |
| Q37 | varchar |  |  | SI | Precautionary measures during recovery |
| Q38 | varchar |  |  | SI | Ice treatment performed |
| Q39 | varchar |  |  | SI | Stairs practiced |
| Q40 | varchar |  |  | SI | Stairs comment |
| Q41 | varchar |  |  | SI | Bike exercise performed |
| Q42 | varchar |  |  | SI | Bike exercise comment |
| Q43 | varchar |  |  | SI | Auscultation performed |
| Q44 | varchar |  |  | SI | Auscultation |
| Q45 | varchar |  |  | SI | Sternal precautions |
| Q46 | varchar |  |  | SI | Incentive spirometer details |
| Q47 | varchar |  |  | SI | Thoracic mobility |
| Q48 | varchar |  |  | SI | Commence neck and shoulder ROM |
| Q49 | varchar |  |  | SI | Neck mobility exercises performed |
| Q50 | varchar |  |  | SI | Neck mobility comments |
| Q51 | varchar |  |  | SI | Trismus prevention exercises performed |
| Q52 | varchar |  |  | SI | Trismus prevention comments |
| Q53 | varchar |  |  | SI | Shoulder mobility exercise performed |
| Q54 | varchar |  |  | SI | Shoulder mobility comments |
| Q55 | varchar |  |  | SI | Head & neck exercises performed |
| Q56 | varchar |  |  | SI | Head & neck exercise program comments |
| Q57 | varchar |  |  | SI | Exercise intensity |
| Q58 | varchar |  |  | SI | Education |
| Q59 | varchar |  |  | SI | Deep breathing exercises |
| Q60 | varchar |  |  | SI | Supported huff / cough |
| Q61 | varchar |  |  | SI | Review bed exercises |
| Q63 | varchar |  |  | SI | Log roll transfers |
| Q63ObsDR | varchar |  | FK | SI | Log roll transfers DR |
| Q64 | varchar |  |  | SI | Log roll transfer comments |
| Q65 | varchar |  |  | SI | Respiratory assessment |
| Q66 | varchar |  |  | SI | Treatment summary |
| Q67 | varchar |  |  | SI | Plan |
| Q68 | varchar |  |  | SI | Post operative  instructions |
| Q69 | varchar |  |  | SI | Equipment |
| Q70 | varchar |  |  | SI | Home exercise program |
| Q71 | varchar |  |  | SI | Physiotherapy referral required |
| Q72 | varchar |  |  | SI | Estimated discharge date |
| Q73 | varchar |  |  | SI | Pain at rest |
| Q73ObsDR | varchar |  | FK | SI | Pain at rest DR |
| Q74 | varchar |  |  | SI | Pain on movement |
| Q74ObsDR | varchar |  | FK | SI | Pain on movement DR |
| Q75 | varchar |  |  | SI | Analgesia |
| Q75ObsDR | varchar |  | FK | SI | Analgesia DR |
| Q76 | varchar |  |  | SI | NIBP Systolic |
| Q76ObsDR | varchar |  | FK | SI | NIBP Systolic DR |
| Q77 | varchar |  |  | SI | NIBP Diastolic |
| Q77ObsDR | varchar |  | FK | SI | NIBP Diastolic DR |
| Q78 | varchar |  |  | SI | Oxygen Saturation |
| Q78ObsDR | varchar |  | FK | SI | Oxygen Saturation DR |
| Q79 | varchar |  |  | SI | Hb |
| Q79ObsDR | varchar |  | FK | SI | Hb DR |
| Q80 | varchar |  |  | SI | Weight bearing |
| Q80ObsDR | varchar |  | FK | SI | Weight bearing DR |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*