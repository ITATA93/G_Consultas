# SQLUser.OR_PreanaestheticConsult

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORPRE_RowId | bigint | PK |  | NO | - |
| ORPRE_ASA_DR | bigint |  | FK | SI | Des Ref to ORC ASA |
| ORPRE_Adm_DR | bigint |  | FK | SI | PAAdm assigned to  |
| ORPRE_AnaestMethods | varchar |  |  | SI | List of Anaesthetic Methods |
| ORPRE_Anaesthetist_DR | varchar |  | FK | SI | Anaesthetist Des Ref to CTCP |
| ORPRE_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| ORPRE_Method | bigint |  |  | SI | Method of Anaest. |
| ORPRE_No | varchar |  |  | SI | Anaesthesia No |
| ORPRE_ObsOnAdm_DR | varchar |  | FK | SI | Observations on admission |
| ORPRE_OperatingRoom_DR | bigint |  | FK | SI | DR RBOperatingRoom |
| ORPRE_Patient_DR | bigint |  | FK | SI | PAPerson created for (PAPerson) |
| ORPRE_PreAnaAssessAirwayDent | varchar |  |  | SI | Pre-anaesthetic assessment airway/dentition |
| ORPRE_PreAnaAssessAnaesthetist_DR | varchar |  | FK | SI | Pre-anaesthetic assessment anaesthetist |
| ORPRE_PreAnaAssessDate | date |  |  | SI | Pre-anaesthetic assessment date |
| ORPRE_PreAnaAssessHistory | varchar |  |  | SI | Pre-anaesthetic assessment history |
| ORPRE_PreAnaAssessInfAnaRisk | varchar |  |  | SI | Pre-anaesthetic assessment informed of anaesthetic... |
| ORPRE_PreAnaAssessOther | varchar |  |  | SI | Pre-anaesthetic assessment other |
| ORPRE_PreAnaAssessPlan | varchar |  |  | SI | Pre-anaesthetic assessment plan |
| ORPRE_ProposedProcedure | varchar |  |  | SI | Proposed Procedure |
| ORPRE_Status | varchar |  |  | SI | Preanaesthetic Status |
| ORPRE_TextArea1 | varchar |  |  | SI | Text Area 1 |
| ORPRE_TextArea2 | varchar |  |  | SI | Text Area 2 |
| ORPRE_TextArea3 | varchar |  |  | SI | Text Area 3 |
| ORPRE_TextArea4 | varchar |  |  | SI | Text Area 4 |
| Q01 | - |  |  | SI | Domestic and family violence alert completed |
| Q02 | - |  |  | SI | Interpreter required |
| Q03 | - |  |  | SI | Preferred language spoken |
| Q04 | - |  |  | SI | Preferred interpreter |
| Q05 | - |  |  | SI | Type of domestic & family violence (D&FV) |
| Q06 | - |  |  | SI | Other type |
| Q07 | - |  |  | SI | Alleged perpetrator relationship to patient |
| Q08 | - |  |  | SI | Other perpetrator |
| Q09 | - |  |  | SI | Patient's report of situation |
| Q10 | - |  |  | SI | Clinician's assessment of situation |
| Q11 | - |  |  | SI | Children / Other in the family |
| Q12 | - |  |  | SI | Location / Residence of children |
| Q13 | - |  |  | SI | Legal status |
| Q14 | - |  |  | SI | Date and time of incident |
| Q15 | - |  |  | SI | Date |
| Q16 | - |  |  | SI | Time |
| Q17 | - |  |  | SI | Unknown |
| Q18 | - |  |  | SI | N/A |
| Q19 | - |  |  | SI | History of FV |
| Q20 | - |  |  | SI | Client's living arrangements |
| Q21 | - |  |  | SI | Identified risks |
| Q22 | - |  |  | SI | Patient / Client |
| Q23 | - |  |  | SI | Perpetrator risks (e.g. use of weapons, threats to... |
| Q24 | - |  |  | SI | Relationship |
| Q25 | - |  |  | SI | Other relationship |
| Q26 | - |  |  | SI | Safety |
| Q27 | - |  |  | SI | Clinician assessed urgency for action |
| Q28 | - |  |  | SI | Safety threat to treating team identified (Inform ... |
| Q29 | - |  |  | SI | Referral consent |
| Q30 | - |  |  | SI | Consent obtained to provide details to external se... |
| Q31 | - |  |  | SI | Internal referral |
| Q32 | - |  |  | SI | External referrals |
| Q33 | - |  |  | SI | Information (brochures / numbers) provided |
| Q34 | - |  |  | SI | Safety plan |
| Q35 | - |  |  | SI | Client discharged to |
| Q36 | - |  |  | SI | Client wishes considered in discharge planning |
| Q37 | - |  |  | SI | Notes |
| Q38 | - |  |  | SI | If other, please specify |
| Q39 | - |  |  | SI | Other agency |
| Q40 | - |  |  | SI | Other living arrangements |
| Q41 | - |  |  | SI | Interpreter required |
| Q42 | - |  |  | SI | Preferred language spoken |
| Q43 | - |  |  | SI | Other internal referral |
| Q44 | - |  |  | SI | Name |
| Q45 | - |  |  | SI | Designation / Service |
| Q46 | - |  |  | SI | Secondary Consultation Sought |
| Q47 | - |  |  | SI | Date |
| Q48 | - |  |  | SI | Time |
| Q49 | - |  |  | SI | External link |
| Q50 | - |  |  | SI | Unknown |
| Q51 | - |  |  | SI | N/A |
| Q52 | - |  |  | SI | Children / other in the family notes |
| Q53 | - |  |  | SI | Family safety framework assessment required |
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