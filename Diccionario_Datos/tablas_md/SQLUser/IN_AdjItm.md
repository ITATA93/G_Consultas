# SQLUser.IN_AdjItm

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INADI_INAD_ParRef | bigint | PK |  | NO | Des Ref To INAD |
| INADI_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INADI_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| INADI_ChildSub | numeric |  |  | NO | INADI ChildSub (New Key) |
| INADI_INCLB_DR | varchar |  | FK | NO | Des Ref to INCLB |
| INADI_INSTI_DR | varchar |  | FK | SI | Des Ref to INSTI |
| INADI_Qty | double |  |  | SI | Quantity |
| INADI_RowId | varchar |  |  | NO | - |
| INADI_UCost | double |  |  | NO | Unit Cost |
| Q01 | - |  |  | SI | Photographed / audio-video recorded	 |
| Q02 | - |  |  | SI | And/or study models of mouth being taken	 |
| Q03 | - |  |  | SI | Clinical management	 |
| Q04 | - |  |  | SI | Education |
| Q05 | - |  |  | SI | Publication & research	 |
| Q06 | - |  |  | SI | Other	 |
| Q07 | - |  |  | SI | Health professional to specify	 |
| Q08 | - |  |  | SI | Signature	 |
| Q08UDt | - |  |  | SI | Signature	 Last Updated Date |
| Q08UTm | - |  |  | SI | Signature	 Last Updated Time |
| Q09 | - |  |  | SI | They may be used to help plan and evaluate care, c... |
| Q10 | - |  |  | SI | The images will form part of your confidential med... |
| Q11 | - |  |  | SI | Images may also be seen by health professionals fo... |
| Q12 | - |  |  | SI | They may be used during talks, conference presenta... |
| Q13 | - |  |  | SI | This may involve images being used, for example in... |
| Q14 | - |  |  | SI | Images will be seen by health professionals who ac... |
| Q15 | - |  |  | SI | They may also be seen by the general public. All i... |
| Q16 | - |  |  | SI | I have been given the opportunity to ask questions... |
| Q17 | - |  |  | SI | I consent to myself / patient listed above being |
| Q18 | - |  |  | SI | For the purposes of: |
| Q19 | - |  |  | SI | Name of person signing (if not the patient) |
| Q20 | - |  |  | SI | Relationship to patient |
| Q21 | - |  |  | SI | Reason patient unable to sign |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | Images will only be seen by treating health profes... |
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