# SQLUser.OR_AnaestPatPosition

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATPOS_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| PATPOS_Childsub | double |  |  | NO | Childsub |
| PATPOS_Position_DR | bigint |  | FK | SI | Des Ref ORCOperPosition |
| PATPOS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Standard Directions : One trial of each test item ... |
| Q02 | - |  |  | SI | Standard Starting Position: |
| Q03 | - |  |  | SI | Thights should be positioned in neutral hip abduct... |
| Q04 | - |  |  | SI | Date |
| Q05 | - |  |  | SI | Time |
| Q06 | - |  |  | SI | Anterior nudge (light pressure x 1, at sternum) |
| Q07 | - |  |  | SI | Posterior Nudge: between scapular spines |
| Q08 | - |  |  | SI | Lateral Nudge: to dominant side at acromion |
| Q09 | - |  |  | SI | Static sitting: 30 seconds |
| Q10 | - |  |  | SI | Sitting, move head side to side (node ''no'') |
| Q11 | - |  |  | SI | Sitting, eyes closed: 30 seconds |
| Q12 | - |  |  | SI | Sitting, lift foot 1 inch twice |
| Q13 | - |  |  | SI | Pick up object from behind |
| Q14 | - |  |  | SI | Forward reach |
| Q15 | - |  |  | SI | Lateral reach |
| Q16 | - |  |  | SI | Pick up object from floor |
| Q17 | - |  |  | SI | Posterior scooting |
| Q18 | - |  |  | SI | Anterior scooting |
| Q19 | - |  |  | SI | Lateral scooting |
| Q20 | - |  |  | SI | Posterior nudge: Without warning, at any time duri... |
| Q21 | - |  |  | SI | Lateral nudge: Without warning, at any time during... |
| Q22 | - |  |  | SI | Static sitting: Sit with your hands in your lap fo... |
| Q23 | - |  |  | SI | Remain sitting steady and tall without using your ... |
| Q24 | - |  |  | SI | Keep looking to the right until I tell you “look l... |
| Q25 | - |  |  | SI | Keep your head to the left until I tell you, ''loo... |
| Q26 | - |  |  | SI | Sitting, lift foot (scored once for least involved... |
| Q27 | - |  |  | SI | Turn and pick up object from behind in preferred d... |
| Q28 | - |  |  | SI | (Object placed in midline, one hand’s breadth ''ﬁn... |
| Q29 | - |  |  | SI | Reach forward with outstretched hand at shoulder h... |
| Q30 | - |  |  | SI | (Perform passively to assess range of motion |
| Q31 | - |  |  | SI | Lateral reach with hand at shoulder height: Reach ... |
| Q32 | - |  |  | SI | Be sure to get all your weight off the opposite si... |
| Q33 | - |  |  | SI | (Completes full, available range of motion maintai... |
| Q34 | - |  |  | SI | and clearance of contralateral ischial tuberosity ... |
| Q35 | - |  |  | SI | Pick object up off ﬂoor: Pick this object up off t... |
| Q36 | - |  |  | SI | &nbsp |
| Q37 | - |  |  | SI | Anterior scooting (2′′): Move forward 2 inches wit... |
| Q38 | - |  |  | SI | Lateral scooting (2′′, scored once for preferred d... |
| Q39 | - |  |  | SI | Sitting, eyes closed: Close your eyes and remain s... |
| Q40 | - |  |  | SI | Person seated at edge of standard hospital bed (no... |
| Q41 | - |  |  | SI | Anterior nudge: Without warning, at any time durin... |
| Q42 | - |  |  | SI | Gorman SL, Radtka S, Melnick ME, Abrams GM, Byl NN... |
| Q43 | - |  |  | SI | J Neurol Phys Ther. 2010 |
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