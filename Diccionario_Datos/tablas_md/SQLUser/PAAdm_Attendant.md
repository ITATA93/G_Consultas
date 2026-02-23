# SQLUser.PAAdm_Attendant

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ATD_ParRef | bigint | PK |  | NO | Des Ref to PAAdm |
| ATD_Address1 | varchar |  |  | SI | Address 1 |
| ATD_Address2 | varchar |  |  | SI | Address 2 |
| ATD_Childsub | double |  |  | NO | Childsub |
| ATD_CityCode_DR | bigint |  | FK | SI | Des Ref CityCode |
| ATD_ContactType_DR | bigint |  | FK | SI | Des Ref ContactType |
| ATD_DateFrom | date |  |  | SI | Date From |
| ATD_DateTo | date |  |  | SI | Date To |
| ATD_Email | varchar |  |  | SI | Email |
| ATD_MobPhone | varchar |  |  | SI | Mob Phone |
| ATD_Name | varchar |  |  | SI | Name |
| ATD_Name2 | varchar |  |  | SI | Name2 |
| ATD_Name3 | varchar |  |  | SI | Name3 |
| ATD_Organisation | varchar |  |  | SI | Organisation |
| ATD_OrganisationNumber | varchar |  |  | SI | Carer Contribution |
| ATD_Province_DR | bigint |  | FK | SI | Des Ref Province |
| ATD_RowId | varchar |  |  | NO | - |
| ATD_TelH | varchar |  |  | SI | TelH |
| ATD_TelO | varchar |  |  | SI | TelO |
| ATD_Title_DR | bigint |  | FK | SI | Des Ref Title_DR |
| ATD_UpdateDate | date |  |  | SI | UpdateDate |
| ATD_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| ATD_UpdateTime | time |  |  | SI | UpdateTime |
| ATD_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ATD_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Choose the best answer for how you have felt over ... |
| Q04 | - |  |  | SI | I worry a lot of the time |
| Q05 | - |  |  | SI | I find it difficult to make a decision |
| Q06 | - |  |  | SI | I often feel jumpy |
| Q07 | - |  |  | SI | I find it hard to relax |
| Q08 | - |  |  | SI | I often cannot enjoy things because of my worries |
| Q09 | - |  |  | SI | Little things bother me a lot |
| Q10 | - |  |  | SI | I often feel like I have butterflies in my stomach |
| Q11 | - |  |  | SI | I think of myself as a worrier |
| Q12 | - |  |  | SI | I can't help worrying about even trivial things |
| Q13 | - |  |  | SI | I often feel nervous |
| Q14 | - |  |  | SI | My own thoughts often make me anxious |
| Q15 | - |  |  | SI | I get an upset stomach due to my worrying |
| Q16 | - |  |  | SI | I think of myself as a nervous person |
| Q17 | - |  |  | SI | I always anticipate the worst will happen |
| Q18 | - |  |  | SI | I often feel shaky inside |
| Q19 | - |  |  | SI | I think that my worries interfere with my life |
| Q20 | - |  |  | SI | My worries often overwhelm me |
| Q21 | - |  |  | SI | I sometimes feel a great knot in my stomach |
| Q22 | - |  |  | SI | I miss out on things because I worry too much |
| Q23 | - |  |  | SI | I often feel upset |
| Q24 | - |  |  | SI | Total score |
| Q25 | - |  |  | SI | Pachana NA, Byrne GJ, Siddle H, Koloski N, Harley ... |
| Q26 | - |  |  | SI | The Geriatric Anxiety Inventory (GAI) is a 20-item... |
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