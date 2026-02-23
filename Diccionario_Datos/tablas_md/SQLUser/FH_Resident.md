# SQLUser.FH_Resident

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hogar/Familia**. Registro de datos familiares.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FH_RowId | bigint | PK |  | NO | - |
| FH_Address1 | varchar |  |  | SI | Address 1 |
| FH_Address2 | varchar |  |  | SI | Address 2 |
| FH_AddressType_DR | bigint |  | FK | SI | Des Ref AddresType |
| FH_AppliancesIDs | varchar |  |  | SI | Des Ref Appliances |
| FH_Area_DR | bigint |  | FK | SI | Des Ref Area |
| FH_ChkboxField1 | varchar |  |  | SI | Checkbox Field1 |
| FH_ChkboxField2 | varchar |  |  | SI | Checkbox Field2 |
| FH_CityCode_DR | bigint |  | FK | SI | Des Ref to CTCIT (suburb) |
| FH_DateFrom | date |  |  | NO | Date From |
| FH_DateTo | date |  |  | SI | Date To |
| FH_Electricity | varchar |  |  | SI | Has Electricity |
| FH_Email | varchar |  |  | SI | Email |
| FH_FamilyMoveDate | date |  |  | SI | Date Family moved into the house |
| FH_Freetext1 | varchar |  |  | SI | Freetext1 |
| FH_Freetext2 | varchar |  |  | SI | Freetext2 |
| FH_GarbageDisposal_DR | bigint |  | FK | SI | Des Ref GarbageDisposal |
| FH_MainResidence | varchar |  |  | SI | Email |
| FH_MicroArea_DR | bigint |  | FK | SI | Des Ref MicroArea |
| FH_NoOfRooms | double |  |  | SI | Number of Rooms |
| FH_PatAlert_DR | bigint |  | FK | SI | Des Ref PatientAlert |
| FH_PrimaryResident_DR | bigint |  | FK | SI | Primary Resident |
| FH_Province_DR | bigint |  | FK | SI | Des Ref CT_Province (state) |
| FH_Questionnaire | varchar |  |  | SI | Questionnaire |
| FH_ResidentNo | varchar |  |  | NO | Resident No |
| FH_SanitationTarget_DR | bigint |  | FK | SI | Des Ref Sanitation Target |
| FH_Segment_DR | bigint |  | FK | SI | Des Ref Segment |
| FH_Telphone | varchar |  |  | SI | Telephone No |
| FH_Telphone2 | varchar |  |  | SI | Telephone No 2 |
| FH_UpdateDate | date |  |  | SI | UpdateDate |
| FH_UpdateTime | time |  |  | SI | Update Time |
| FH_UpdateUser_DR | bigint |  | FK | SI | Des Ref UserUpdate |
| FH_UserAdded_DR | bigint |  | FK | SI | Des Ref UserUpdate |
| FH_WaterSupply_DR | bigint |  | FK | SI | Des Ref Water Supply |
| FH_WaterTreatment_DR | bigint |  | FK | SI | Des Ref Water Treatment |
| FH_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP (postcode) |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bag / Mask and oxygen flow checked |
| Q04 | - |  |  | SI | Emergency IV port identified / PIVC in situ |
| Q05 | - |  |  | SI | Suction equipment present and functional |
| Q06 | - |  |  | SI | All equipment plugged in and functional |
| Q07 | - |  |  | SI | Medication orders reviewed (infusion rates) |
| Q08 | - |  |  | SI | Monitor alarm limits checked |
| Q09 | - |  |  | SI | Equipment changes |
| Q10 | - |  |  | SI | Yankauer sucker and tubing (changed daily) |
| Q11 | - |  |  | SI | Hiflow / BiPAP circuit (changed weekly) |
| Q12 | - |  |  | SI | Due date - Hiflow / BiPAP circuit change |
| Q13 | - |  |  | SI | Humidified water bag changed |
| Q14 | - |  |  | SI | ID bands checked and on patient |
| Q15 | - |  |  | SI | Falls risk assessment completed |
| Q16 | - |  |  | SI | Pressure injury risk and skin assessment (every sh... |
| Q17 | - |  |  | SI | Delirium risk assessment completed |
| Q18 | - |  |  | SI | Wound chart reviewed |
| Q19 | - |  |  | SI | Invasive device reviewed and updated |
| Q20 | - |  |  | SI | TEDS in situ |
| Q21 | - |  |  | SI | Electrocardiogram (ECG) electrodes changed |
| Q22 | - |  |  | SI | Daily 12 lead ECG completed |
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