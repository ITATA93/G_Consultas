# questionnaire.QTCFIST

> "Function in Sitting Test (FIST)	"

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Function in Sitting Test (FIST)	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Standard Directions : One trial of each test item ... |
| Q02 | varchar |  |  | SI | Standard Starting Position: |
| Q03 | varchar |  |  | SI | Thights should be positioned in neutral hip abduct... |
| Q04 | date |  |  | SI | Date |
| Q05 | time |  |  | SI | Time |
| Q06 | varchar |  |  | SI | Anterior nudge (light pressure x 1, at sternum) |
| Q07 | varchar |  |  | SI | Posterior Nudge: between scapular spines |
| Q08 | varchar |  |  | SI | Lateral Nudge: to dominant side at acromion |
| Q09 | varchar |  |  | SI | Static sitting: 30 seconds |
| Q10 | varchar |  |  | SI | Sitting, move head side to side (node ''no'') |
| Q11 | varchar |  |  | SI | Sitting, eyes closed: 30 seconds |
| Q12 | varchar |  |  | SI | Sitting, lift foot 1 inch twice |
| Q13 | varchar |  |  | SI | Pick up object from behind |
| Q14 | varchar |  |  | SI | Forward reach |
| Q15 | varchar |  |  | SI | Lateral reach |
| Q16 | varchar |  |  | SI | Pick up object from floor |
| Q17 | varchar |  |  | SI | Posterior scooting |
| Q18 | varchar |  |  | SI | Anterior scooting |
| Q19 | varchar |  |  | SI | Lateral scooting |
| Q20 | varchar |  |  | SI | Posterior nudge: Without warning, at any time duri... |
| Q21 | varchar |  |  | SI | Lateral nudge: Without warning, at any time during... |
| Q22 | varchar |  |  | SI | Static sitting: Sit with your hands in your lap fo... |
| Q23 | varchar |  |  | SI | Remain sitting steady and tall without using your ... |
| Q24 | varchar |  |  | SI | Keep looking to the right until I tell you “look l... |
| Q25 | varchar |  |  | SI | Keep your head to the left until I tell you, ''loo... |
| Q26 | varchar |  |  | SI | Sitting, lift foot (scored once for least involved... |
| Q27 | varchar |  |  | SI | Turn and pick up object from behind in preferred d... |
| Q28 | varchar |  |  | SI | (Object placed in midline, one hand’s breadth ''ﬁn... |
| Q29 | varchar |  |  | SI | Reach forward with outstretched hand at shoulder h... |
| Q30 | varchar |  |  | SI | (Perform passively to assess range of motion; must... |
| Q31 | varchar |  |  | SI | Lateral reach with hand at shoulder height: Reach ... |
| Q32 | varchar |  |  | SI | Be sure to get all your weight off the opposite si... |
| Q33 | varchar |  |  | SI | (Completes full, available range of motion maintai... |
| Q34 | varchar |  |  | SI | and clearance of contralateral ischial tuberosity ... |
| Q35 | varchar |  |  | SI | Pick object up off ﬂoor: Pick this object up off t... |
| Q36 | varchar |  |  | SI | &nbsp;Posterior scooting (2′′): Move backward 2 in... |
| Q37 | varchar |  |  | SI | Anterior scooting (2′′): Move forward 2 inches wit... |
| Q38 | varchar |  |  | SI | Lateral scooting (2′′, scored once for preferred d... |
| Q39 | varchar |  |  | SI | Sitting, eyes closed: Close your eyes and remain s... |
| Q40 | varchar |  |  | SI | Person seated at edge of standard hospital bed (no... |
| Q41 | varchar |  |  | SI | Anterior nudge: Without warning, at any time durin... |
| Q42 | varchar |  |  | SI | Gorman SL, Radtka S, Melnick ME, Abrams GM, Byl NN... |
| Q43 | varchar |  |  | SI | J Neurol Phys Ther. 2010;34(3):150-160. doi:10.109... |
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