# SQLUser.OEC_ResultEscalation

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ESC_RowId | bigint | PK |  | NO | - |
| ESC_ARCIM_DR | varchar |  | FK | SI | Order Item - No core function |
| ESC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ESC_Code | varchar |  |  | NO | Code |
| ESC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ESC_CreatedDate | date |  |  | SI | Created Date |
| ESC_CreatedTime | time |  |  | SI | Created Time |
| ESC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ESC_DateFrom | date |  |  | SI | Date From |
| ESC_DateTo | date |  |  | SI | Date To |
| ESC_Desc | varchar |  |  | NO | Description |
| ESC_Epissubtype_DR | bigint |  | FK | SI | Episode SubType - No core function |
| ESC_HeadDepDays | double |  |  | SI | Head of Dep Days |
| ESC_HeadDepGrpDays | double |  |  | SI | Head of Dep Grp Days |
| ESC_HeadDivDays | double |  |  | SI | Head of Div Days |
| ESC_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ESC_ItemCat_DR | bigint |  | FK | SI | Order Subcategory - No core function |
| ESC_MainCPDays | double |  |  | SI | Main CP Days |
| ESC_MedSuperintDays | double |  |  | SI | Med Superint Days |
| ESC_Message | varchar |  |  | SI | Message - No core function |
| ESC_NotificationMethod | varchar |  |  | SI | Notification Method  - No core function |
| ESC_OrdCat_DR | bigint |  | FK | SI | Order Category - No core function |
| ESC_Owner | varchar |  |  | SI | Owner |
| ESC_Recipient_DR | varchar |  | FK | SI | Recipient - No core function |
| ESC_RespUnit_DR | bigint |  | FK | SI | Responsible Unit - No core function |
| ESC_ResultFlags | varchar |  |  | SI | Result Flags  - No core function |
| ESC_SPDays | double |  |  | SI | SP Days |
| ESC_TimeElapsed | double |  |  | SI | Time Elapsed - No core function |
| ESC_TimeUnit | varchar |  |  | SI | Time Unit  - No core function |
| ESC_UpdatedDate | date |  |  | SI | Updated Date |
| ESC_UpdatedTime | time |  |  | SI | Updated Time |
| ESC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ESC_Urgent | varchar |  |  | SI | Urgent - No core function |
| ESC_Ward_DR | bigint |  | FK | SI | Ward - No core function |
| Q01 | - |  |  | SI | Rectum |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Rectum DR |
| Q03 | - |  |  | SI | Faecal impaction |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Faecal impaction DR |
| Q05 | - |  |  | SI | Melena |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Melena DR |
| Q07 | - |  |  | SI | Bright red blood |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Bright red blood DR |
| Q09 | - |  |  | SI | Mass |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Mass DR |
| Q11 | - |  |  | SI | Hemorrhoids |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Hemorrhoids DR |
| Q13 | - |  |  | SI | Sphincter tone |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Sphincter tone DR |
| Q15 | - |  |  | SI | Perianal fistula |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Perianal fistula DR |
| Q17 | - |  |  | SI | Abscess |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Abscess DR |
| Q19 | - |  |  | SI | Pilonidal Sinus |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Pilonidal Sinus DR |
| Q21 | - |  |  | SI | Prostate |
| Q21C | - |  |  | SI | Consistency |
| Q21L | - |  |  | SI | Limits |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Prostate DR |
| Q21P | - |  |  | SI | Pain |
| Q21S | - |  |  | SI | Size |
| Q21SU | - |  |  | SI | Surface |
| Q29 | - |  |  | SI | Seminal vesicles |
| Q29N | - |  |  | SI | Note |
| Q31 | - |  |  | SI | Anal fissures |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Anal fissures DR |
| Q33 | - |  |  | SI | Cervix |
| Q33N | - |  |  | SI | Note |
| Q33ObsDR | - |  |  | SI | Cervix DR |
| Q35 | - |  |  | SI | Uterus |
| Q35N | - |  |  | SI | Note |
| Q35ObsDR | - |  |  | SI | Uterus DR |
| Q37 | - |  |  | SI | Parameters |
| Q37N | - |  |  | SI | Note |
| Q37ObsDR | - |  |  | SI | Parameters DR |
| Q39 | - |  |  | SI | Annexes |
| Q39N | - |  |  | SI | Note |
| Q39ObsDR | - |  |  | SI | Annexes DR |
| Q41 | - |  |  | SI | Douglas and pelvis |
| Q41N | - |  |  | SI | Note |
| Q41ObsDR | - |  |  | SI | Douglas and pelvis DR |
| Q42 | - |  |  | SI | Other |
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