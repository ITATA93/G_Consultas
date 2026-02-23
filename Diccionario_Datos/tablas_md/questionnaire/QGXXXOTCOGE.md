# questionnaire.QGXXXOTCOGE

> Operation Consent Generic

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Operation Consent Generic

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q03 | varchar |  |  | SI | Treatment / Procedure / Operations / Investigation... |
| Q04 | varchar |  |  | SI | List the treatment(s)/ operation(s)/ investigation... |
| Q04a | varchar |  |  | SI | List the treatment(s)/ procedure(s)/ investigation... |
| Q05 | varchar |  |  | SI | This procedure may require |
| Q06 | varchar |  |  | SI | Doctor |
| Q08 | longvarbinary |  |  | SI | Signature Doctor |
| Q08UDt | date |  |  | SI | Signature Doctor Last Updated Date |
| Q08UTm | time |  |  | SI | Signature Doctor Last Updated Time |
| Q09 | varchar |  |  | SI | Laterality: Note which side of the body the proced... |
| Q10 | varchar |  |  | SI | Any extra procedures that might become necessary d... |
| Q10a | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | The following information leaflet has been provide... |
| Q12 | varchar |  |  | SI | Creutzfeldt Jakob disease (CJD) |
| Q13 | varchar |  |  | SI | Have you ever been notified that you are at risk o... |
| Q14 | varchar |  |  | SI | Photography, Audio or Visual Recording |
| Q15 | varchar |  |  | SI | I agree to the use of any of the above type of rec... |
| Q16 | varchar |  |  | SI | I agree to unidentified versions of any of the abo... |
| Q17 | varchar |  |  | SI | Medical Training |
| Q18 | varchar |  |  | SI | I agree to the involvement of medical and other st... |
| Q19 | varchar |  |  | SI | Use of Tissue |
| Q20 | varchar |  |  | SI | I agree that tissue (including blood) not needed f... |
| Q21 | varchar |  |  | SI | Where additional clinical information is needed fo... |
| Q22 | varchar |  |  | SI | I have informed the patient of the treatment optio... |
| Q23 | varchar |  |  | SI | I have recommended the treatment(s) / procedure(s)... |
| Q24 | varchar |  |  | SI | I have explained the treatment(s) / procedure(s) /... |
| Q25 | varchar |  |  | SI | I have provided the patient with information speci... |
| Q26 | varchar |  |  | SI | I have given the patient the opportunity to discus... |
| Q27 | varchar |  |  | SI | The doctor has explained my medical condition and ... |
| Q28 | varchar |  |  | SI | The risks of the procedure have been explained to ... |
| Q30 | varchar |  |  | SI | I understand that the result / outcome of the trea... |
| Q31 | varchar |  |  | SI | I understand that if immediate life-threating even... |
| Q32 | varchar |  |  | SI | I consent to undergo the procedure(s) treatment(s)... |
| Q33 | varchar |  |  | SI | My questions have been answered to my satisfaction... |
| Q34 | varchar |  |  | SI | Any procedures that the patient DOES NOT wish to b... |
| Q35 | varchar |  |  | SI | I have read and understood the Patient Information... |
| Q36 | longvarbinary |  |  | SI | Signed Patient |
| Q36UDt | date |  |  | SI | Signed Patient Last Updated Date |
| Q36UTm | time |  |  | SI | Signed Patient Last Updated Time |
| Q37 | varchar |  |  | SI | Signing for a child or young person |
| Q37a | varchar |  |  | SI | I confirm I am a person with parental / guardiansh... |
| Q37b | longvarbinary |  |  | SI | Signed (Parent / guardian) |
| Q37bUDt | date |  |  | SI | Signed (Parent / guardian) Last Updated Date |
| Q37bUTm | time |  |  | SI | Signed (Parent / guardian) Last Updated Time |
| Q37c | varchar |  |  | SI | Name (Parent / guardian) |
| Q37d | varchar |  |  | SI | Relationship to patient |
| Q40 | varchar |  |  | SI | If the patient is unable to sign but has indicated... |
| Q41 | longvarbinary |  |  | SI | Signed (Witness) |
| Q41UDt | date |  |  | SI | Signed (Witness) Last Updated Date |
| Q41UTm | time |  |  | SI | Signed (Witness) Last Updated Time |
| Q41c | varchar |  |  | SI | Name of witness |
| Q45 | varchar |  |  | SI | Confirmation of consent |
| Q46 | varchar |  |  | SI | Confirmation of consent (where the treatment / pro... |
| Q46a | varchar |  |  | SI | and consents to the treatment |
| Q47 | longvarbinary |  |  | SI | Signed (Care Provider) |
| Q47UDt | date |  |  | SI | Signed (Care Provider) Last Updated Date |
| Q47UTm | time |  |  | SI | Signed (Care Provider) Last Updated Time |
| Q49 | varchar |  |  | SI | Name |
| Q50 | varchar |  |  | SI | Interpreter’s statement |
| Q51 | varchar |  |  | SI | I have interpreted the information to the best of ... |
| Q52 | longvarbinary |  |  | SI | Signed (Interpreter) |
| Q52UDt | date |  |  | SI | Signed (Interpreter) Last Updated Date |
| Q52UTm | time |  |  | SI | Signed (Interpreter) Last Updated Time |
| Q52c | varchar |  |  | SI | Name  |
| Q52d | varchar |  |  | SI | Or, please note the intepreter service reference I... |
| Q56 | varchar |  |  | SI | Withdrawal of patient consent |
| Q56b | bit |  |  | SI | The patient has withdrawn consent (Check this box ... |
| Q56c | longvarbinary |  |  | SI | Signed (Patient) |
| Q56cUDt | date |  |  | SI | Signed (Patient) Last Updated Date |
| Q56cUTm | time |  |  | SI | Signed (Patient) Last Updated Time |
| Q56d | varchar |  |  | SI | Reason given to withdraw consent (if known) |
| Q56e | longvarbinary |  |  | SI | Signed (Care Provider) |
| Q56eUDt | date |  |  | SI | Signed (Care Provider) Last Updated Date |
| Q56eUTm | time |  |  | SI | Signed (Care Provider) Last Updated Time |
| Q61 | date |  |  | SI | Date |
| Q62 | varchar |  |  | SI | Name (CP) |
| Q63 | varchar |  |  | SI | I hereby authorize and consent to the presence of ... |
| Q63a | varchar |  |  | SI | They have no role or responsibility in performing ... |
| Q64 | time |  |  | SI | Time |
| Q65 | varchar |  |  | SI | Planned operation |
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