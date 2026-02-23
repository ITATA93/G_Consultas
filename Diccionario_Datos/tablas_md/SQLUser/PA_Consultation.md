# SQLUser.PA_Consultation

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_RowId | bigint | PK |  | NO | - |
| CONS_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| CONS_Assessment | varchar |  |  | SI | Assessment |
| CONS_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CONS_ConsCategGroups_DR | bigint |  | FK | SI | Des Ref PACConsCategGroups |
| CONS_ConsCategory_DR | bigint |  | FK | SI | Des Ref ConsCategory |
| CONS_CreateDate | date |  |  | SI | Create Date |
| CONS_CreateHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| CONS_CreateTime | time |  |  | SI | Create Time |
| CONS_CreateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| CONS_Objective | varchar |  |  | SI | Objective |
| CONS_PAAdm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| CONS_Planning | varchar |  |  | SI | Planning |
| CONS_ReasonForVisit | varchar |  |  | SI | ReasonForVisit |
| CONS_Status | varchar |  |  | SI | Status |
| CONS_Subjective | varchar |  |  | SI | Subjective |
| CONS_UpdateDate | date |  |  | SI | Update Date |
| CONS_UpdateHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| CONS_UpdateTime | time |  |  | SI | Update Time |
| CONS_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| CONS_VisitDate | date |  |  | SI | Visit Date |
| CONS_VisitTime | time |  |  | SI | Visit Time |
| Q01 | - |  |  | SI | Chief Complaint Details |
| Q02 | - |  |  | SI | Duration |
| Q03 | - |  |  | SI | Sudden |
| Q04 | - |  |  | SI | Comments |
| Q05 | - |  |  | SI | Course |
| Q06 | - |  |  | SI | Impact Of Complaint On The Patient |
| Q07 | - |  |  | SI | VHI-10 |
| Q08 | - |  |  | SI | Etiological Factors |
| Q09 | - |  |  | SI | Occupation |
| Q10 | - |  |  | SI | Vocal Demand |
| Q11 | - |  |  | SI | Job Environment |
| Q16 | - |  |  | SI | Examination |
| Q17 | - |  |  | SI | Auditory Perceptual Assessment (APA) |
| Q18 | - |  |  | SI | Overall Grade |
| Q19 | - |  |  | SI | Comments |
| Q20 | - |  |  | SI | Character (Quality) |
| Q21 | - |  |  | SI | Pitch |
| Q22 | - |  |  | SI | Register - Habitual |
| Q23 | - |  |  | SI | Register Break |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Loudness |
| Q26 | - |  |  | SI | Glottal Attack |
| Q28 | - |  |  | SI | External Laryngeal Examination |
| Q29 | - |  |  | SI | Laryngeal Skeleton |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Laryngeal Click |
| Q32 | - |  |  | SI | Laryngeal Position |
| Q33 | - |  |  | SI | Cervical Veins |
| Q34 | - |  |  | SI | Neck Scars |
| Q35 | - |  |  | SI | Type |
| Q36 | - |  |  | SI | Site |
| Q37 | - |  |  | SI | Size |
| Q38 | - |  |  | SI | Tracheostomy |
| Q38ObsDR | - |  |  | SI | Tracheostomy DR |
| Q39 | - |  |  | SI | Tracheostomy Size |
| Q39ObsDR | - |  |  | SI | Tracheostomy Size DR |
| Q40 | - |  |  | SI | Tracheostomy Type |
| Q40ObsDR | - |  |  | SI | Tracheostomy Type DR |
| Q41 | - |  |  | SI | Tracheostomy Cuff |
| Q41ObsDR | - |  |  | SI | Tracheostomy Cuff DR |
| Q42 | - |  |  | SI | Tracheostomy Fenestration |
| Q42ObsDR | - |  |  | SI | Tracheostomy Fenestration DR |
| Q43 | - |  |  | SI | Tracheostomy Speaking Valve |
| Q43ObsDR | - |  |  | SI | Tracheostomy Speaking Valve DR |
| Q44 | - |  |  | SI | Tracheostomy Speaking Valve Type |
| Q45 | - |  |  | SI | Investigations |
| Q46 | - |  |  | SI | CT Head And Neck With Contrast |
| Q47 | - |  |  | SI | CT Head And Neck Without Contrast |
| Q48 | - |  |  | SI | CT Head And Neck And Upper Chest With Contrast |
| Q49 | - |  |  | SI | CT Head And Neck And Upper Chest Without Contrast |
| Q50 | - |  |  | SI | MRI Brain |
| Q51 | - |  |  | SI | Pharyngeal PH |
| Q52 | - |  |  | SI | 24-Hr Double-Probe PH-Metry |
| Q53 | - |  |  | SI | Upper GIT Endoscopy |
| Q54 | - |  |  | SI | Others |
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