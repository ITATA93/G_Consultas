# SQLUser.PA_ConsultationLink

**Schema:** SQLUser
**Columnas:** 173
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_RowId | bigint | PK |  | NO | - |
| LINK_ConsCategory_DR | bigint |  | FK | SI | Des Ref ConsCategory |
| LINK_DateCreated | date |  |  | SI | DateCreated |
| LINK_MRDiagnos_DR | varchar |  | FK | SI | Des Ref MRDiagnos |
| LINK_MREvolution_DR | varchar |  | FK | SI | Des Ref MREvolution |
| LINK_MRMedication_DR | varchar |  | FK | SI | Des Ref MRMedication |
| LINK_MRNursingNotes_DR | varchar |  | FK | SI | Des Ref MRNursingNotes |
| LINK_MRObjFind_DR | varchar |  | FK | SI | Des Ref MRObjFind |
| LINK_MRObservations_DR | varchar |  | FK | SI | Des Ref MRObservations |
| LINK_MRPhysExamination_DR | varchar |  | FK | SI | Des Ref MRPhysExamination |
| LINK_MRPictures_DR | varchar |  | FK | SI | Des Ref MRPictures |
| LINK_MRPresentIllness_DR | varchar |  | FK | SI | Des Ref MRPresentIllness |
| LINK_MRProcedures_DR | varchar |  | FK | SI | Des Ref MRProcedures |
| LINK_MRRiskEvaluation_DR | varchar |  | FK | SI | Des Ref MRRiskEvaluation |
| LINK_MRSickNote_DR | varchar |  | FK | SI | Des Ref MRSickNote |
| LINK_MRSubFind_DR | varchar |  | FK | SI | Des Ref MRSubFind |
| LINK_MRSubjectFindings_DR | varchar |  | FK | SI | Des Ref MRSubjectFindings |
| LINK_MRSystemReview_DR | varchar |  | FK | SI | Des Ref MRSystemReview |
| LINK_OEAnnotation_DR | bigint |  | FK | SI | Des Ref OEAnnotation |
| LINK_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| LINK_ORAnaesthesia_DR | varchar |  | FK | SI | Des Ref ORAnaesthesia |
| LINK_ObservationGroup_DR | bigint |  | FK | SI | Des Ref MRCObservationGroup |
| LINK_PAAdmDocument_DR | varchar |  | FK | SI | Des Ref PAAdmDocument |
| LINK_PAAlertMsg_DR | varchar |  | FK | SI | Des Ref PAAlertMsg |
| LINK_PAAllergy_DR | varchar |  | FK | SI | Des Ref PAAllergy |
| LINK_PAConsultation_DR | bigint |  | FK | SI | Des Ref PAConsultation |
| LINK_PADischargeSummary_DR | bigint |  | FK | SI | Des Ref PAAdmDischargeSummary |
| LINK_PALetter_DR | bigint |  | FK | SI | Des Ref PALetter |
| LINK_PAWaitingList_DR | bigint |  | FK | SI | Des Ref PAWaitingList |
| LINK_Questionnaires | varchar |  |  | SI | Questionnaires |
| LINK_TimeCreated | time |  |  | SI | TimeCreated |
| LINK_Type | varchar |  |  | SI | Type |
| Q01 | - |  |  | SI | Venous Thromboembolism (VTE) risk selection |
| Q02 | - |  |  | SI | Risk factors |
| Q03 | - |  |  | SI | Other risk factors |
| Q04 | - |  |  | SI | Contraindications and considerations for pharmacol... |
| Q05 | - |  |  | SI | Other contraindications / considerations for pharm... |
| Q06 | - |  |  | SI | Contraindications for mechanical thromboprophylaxi... |
| Q07 | - |  |  | SI | Other contraindications for mechanical thromboprop... |
| Q08 | - |  |  | SI | Additional details |
| Q09 | - |  |  | SI | In moderate and high risk patients consider contin... |
| Q10 | - |  |  | SI | Risk |
| Q100 | - |  |  | SI | ● Intra operative sequential compression device (S... |
| Q101 | - |  |  | SI | ● Below knee Thrombo - Embolus Deterrents (TED) (a... |
| Q11 | - |  |  | SI | Surgery type |
| Q12 | - |  |  | SI | ● Major - surgery > 45 mins |
| Q13 | - |  |  | SI | ● Minor - all others |
| Q14 | - |  |  | SI | Pharmacological prophylaxis |
| Q15 | - |  |  | SI | Mechanical prophylaxis |
| Q16 | - |  |  | SI | High |
| Q17 | - |  |  | SI | Orthopaedic surgery of the pelvis, hip fracture or... |
| Q18 | - |  |  | SI | ● Major surgery and age > 60 years |
| Q19 | - |  |  | SI | ● Major surgery and age 40 – 60 years and 3 or mor... |
| Q20 | - |  |  | SI | ● Major surgery, any age and previous VTE or activ... |
| Q21 | - |  |  | SI | ● Enoxaparin 40mg* sc nocte 2000 hrs (*use 20mg if... |
| Q22 | - |  |  | SI | OR |
| Q23 | - |  |  | SI | ● Heparin 5000u / 0.2ml sc 8 hourly |
| Q24 | - |  |  | SI | OR |
| Q25 | - |  |  | SI | ● Other |
| Q26 | - |  |  | SI | Please chart all orders in Medication Summary |
| Q27 | - |  |  | SI | ● Post operative foot pumps 48hrs (minimum 24hrs) |
| Q28 | - |  |  | SI | ● Intra operative sequential compression device (S... |
| Q29 | - |  |  | SI | ● Below knee Thrombo - Embolus Deterrents (TED) (a... |
| Q30 | - |  |  | SI | Score |
| Q31 | - |  |  | SI | Classification |
| Q32 | - |  |  | SI | High |
| Q33 | - |  |  | SI | Medium |
| Q34 | - |  |  | SI | Low |
| Q35 | - |  |  | SI | Intent it to reflect the selected risk category wi... |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Time |
| Q38 | - |  |  | SI | Particular patient groups are at an increased risk... |
| Q39 | - |  |  | SI | Moderate |
| Q40 | - |  |  | SI | ● Major surgery and age 40 – 60 years and no risk ... |
| Q41 | - |  |  | SI | ● Major surgery and age < 40 years and 3 or more r... |
| Q42 | - |  |  | SI | ● Minor surgery and age > 60 years |
| Q43 | - |  |  | SI | ● Minor surgery and age 40 – 60 years and 3 or mor... |
| Q44 | - |  |  | SI | ● Enoxaparin 20mg sc nocte 2000 hrs |
| Q45 | - |  |  | SI | OR |
| Q46 | - |  |  | SI | ● Heparin 5000u / 0.2ml sc 12 hourly |
| Q47 | - |  |  | SI | ● Other |
| Q48 | - |  |  | SI | Please chart all orders in medication chart |
| Q49 | - |  |  | SI | Low |
| Q50 | - |  |  | SI | ● Major surgery < 40 years and no risk factors |
| Q51 | - |  |  | SI | ● Minor surgery > 60 years and no risk factors |
| Q52 | - |  |  | SI | Below knee TED’s (optional) |
| Q53 | - |  |  | SI | Risk |
| Q54 | - |  |  | SI | High |
| Q55 | - |  |  | SI | Surgery type |
| Q56 | - |  |  | SI | ● Major - surgery > 45 mins |
| Q57 | - |  |  | SI | ● Minor - all others |
| Q58 | - |  |  | SI | Orthopaedic surgery of the pelvis, hip fracture or... |
| Q59 | - |  |  | SI | ● Major surgery and age > 60 years |
| Q60 | - |  |  | SI | ● Major surgery and age 40 – 60 years and 3 or mor... |
| Q61 | - |  |  | SI | ● Major surgery, any age and previous VTE or activ... |
| Q62 | - |  |  | SI | Pharmacological prophylaxis |
| Q63 | - |  |  | SI | ● Enoxaparin 40mg* sc nocte 2000 hrs (*use 20mg if... |
| Q64 | - |  |  | SI | OR |
| Q65 | - |  |  | SI | ● Heparin 5000u / 0.2ml sc 8 hourly |
| Q66 | - |  |  | SI | OR |
| Q67 | - |  |  | SI | ● Other |
| Q68 | - |  |  | SI | Please chart all orders in Medication Summary |
| Q69 | - |  |  | SI | Mechanical prophylaxis |
| Q70 | - |  |  | SI | ● Post operative foot pumps 48hrs (minimum 24hrs) |
| Q71 | - |  |  | SI | ● Intra operative sequential compression device (S... |
| Q72 | - |  |  | SI | ● Below knee Thrombo - Embolus Deterrents (TED) (a... |
| Q73 | - |  |  | SI | Risk |
| Q74 | - |  |  | SI | Surgery type |
| Q75 | - |  |  | SI | ● Major - surgery > 45 mins |
| Q76 | - |  |  | SI | ● Minor - all others |
| Q77 | - |  |  | SI | ● Major surgery and age 40 – 60 years and no risk ... |
| Q78 | - |  |  | SI | ● Major surgery and age < 40 years and 3 or more r... |
| Q79 | - |  |  | SI | ● Minor surgery and age > 60 years |
| Q80 | - |  |  | SI | ● Minor surgery and age 40 – 60 years and 3 or mor... |
| Q81 | - |  |  | SI | Pharmacological prophylaxis |
| Q82 | - |  |  | SI | ● Enoxaparin 20mg sc nocte 2000 hrs |
| Q83 | - |  |  | SI | OR |
| Q84 | - |  |  | SI | ● Heparin 5000u / 0.2ml sc 12 hourly |
| Q85 | - |  |  | SI | ● Other |
| Q86 | - |  |  | SI | Please chart all orders in medication chart |
| Q87 | - |  |  | SI | Risk |
| Q88 | - |  |  | SI | Low |
| Q89 | - |  |  | SI | Surgery type |
| Q90 | - |  |  | SI | ● Major - surgery > 45 mins |
| Q91 | - |  |  | SI | ● Minor - all others |
| Q92 | - |  |  | SI | ● Major surgery < 40 years and no risk factors |
| Q93 | - |  |  | SI | ● Minor surgery > 60 years and no risk factors |
| Q94 | - |  |  | SI | Pharmacological prophylaxis |
| Q95 | - |  |  | SI | Mechanical Prophylaxis |
| Q96 | - |  |  | SI | Below knee TED’s (optional) |
| Q97 | - |  |  | SI | Moderate |
| Q98 | - |  |  | SI | Mechanical Prophylaxis |
| Q99 | - |  |  | SI | ● Post operative foot pumps 48hrs (minimum 24hrs) |
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