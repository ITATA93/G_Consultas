# SQLUser.OEC_OrderCustomAlerts

**Schema:** SQLUser
**Columnas:** 250
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CUSTALT_RowID | bigint | PK |  | NO | - |
| CUSTALT_AdmLoc_DR | bigint |  | FK | SI | Des Ref to Receiving Location |
| CUSTALT_AdmLocations | varchar |  |  | SI | List of Receiving Locations |
| CUSTALT_AdmType | varchar |  |  | SI | Episode Type |
| CUSTALT_Code | varchar |  |  | SI | Code |
| CUSTALT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CUSTALT_CreatedDate | date |  |  | SI | Created Date |
| CUSTALT_CreatedTime | time |  |  | SI | Created Time |
| CUSTALT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CUSTALT_DateFrom | date |  |  | SI | Date From |
| CUSTALT_DateTo | date |  |  | SI | Date To |
| CUSTALT_DaysInAdvAllowed | varchar |  |  | SI | Days in Advance Allowed for The Order |
| CUSTALT_Desc | varchar |  |  | SI | Description |
| CUSTALT_EndTime | time |  |  | SI | End Time |
| CUSTALT_EpisodeSubType_DR | bigint |  | FK | SI | Episode Subtype |
| CUSTALT_FreqDays | numeric |  |  | SI | Frequency Days |
| CUSTALT_FreqHours | numeric |  |  | SI | Frequency Hours |
| CUSTALT_ItemCat_DR | bigint |  | FK | SI | Des Ref to Order Subcategory |
| CUSTALT_OrdCat_DR | bigint |  | FK | SI | Des Ref to Order Category |
| CUSTALT_OrdDepProcNotes | varchar |  |  | SI | Order Dep Proc Notes Required |
| CUSTALT_OrdDept_DR | bigint |  | FK | SI | Des Ref to Order Location |
| CUSTALT_OrdItem_DR | varchar |  | FK | SI | Des Ref to Order Item |
| CUSTALT_OrdPrios | varchar |  |  | SI | List of Order Priorities |
| CUSTALT_Owner | varchar |  |  | SI | Owner |
| CUSTALT_ReqDocMandatory | varchar |  |  | SI | Requesting Doctor Mandatory |
| CUSTALT_Scenario | varchar |  |  | SI | Scenario |
| CUSTALT_Sex_DR | bigint |  | FK | SI | Des Ref to CTSex |
| CUSTALT_StartTime | time |  |  | SI | Start Time |
| CUSTALT_UpdatedDate | date |  |  | SI | Updated Date |
| CUSTALT_UpdatedTime | time |  |  | SI | Updated Time |
| CUSTALT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tenderness |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Tenderness DR |
| Q02 | - |  |  | SI | Muscle spasm |
| Q02N | - |  |  | SI | Note |
| Q02ObsDR | - |  |  | SI | Muscle spasm DR |
| Q03 | - |  |  | SI | Range of motion |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Range of motion DR |
| Q04 | - |  |  | SI | Spinal Sensory level |
| Q04N | - |  |  | SI | Note |
| Q04ObsDR | - |  |  | SI | Spinal Sensory level DR |
| Q05 | - |  |  | SI | Spinal Motor level |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Spinal Motor level DR |
| Q06 | - |  |  | SI | Shoulder / clavicle |
| Q07 | - |  |  | SI | Tenderness |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Tenderness DR |
| Q08 | - |  |  | SI | Range of motion |
| Q08N | - |  |  | SI | Note |
| Q08ObsDR | - |  |  | SI | Range of motion DR |
| Q09 | - |  |  | SI | Deformity |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Deformity DR |
| Q10 | - |  |  | SI | Distal pulses |
| Q100 | - |  |  | SI | Distal sensation |
| Q100N | - |  |  | SI | Note |
| Q100ObsDR | - |  |  | SI | Distal sensation DR |
| Q102 | - |  |  | SI | Joint stability |
| Q102N | - |  |  | SI | Note |
| Q102ObsDR | - |  |  | SI | Joint stability DR |
| Q104 | - |  |  | SI | Foot |
| Q105 | - |  |  | SI | Tenderness |
| Q105N | - |  |  | SI | Note |
| Q105ObsDR | - |  |  | SI | Tenderness DR |
| Q107 | - |  |  | SI | Range of motion |
| Q107N | - |  |  | SI | Note |
| Q107ObsDR | - |  |  | SI | Range of motion DR |
| Q109 | - |  |  | SI | Deformity |
| Q109N | - |  |  | SI | Note |
| Q109ObsDR | - |  |  | SI | Deformity DR |
| Q10N | - |  |  | SI | Note |
| Q10ObsDR | - |  |  | SI | Distal pulses DR |
| Q11 | - |  |  | SI | Distal sensation |
| Q111 | - |  |  | SI | Capillary refill |
| Q111N | - |  |  | SI | Note |
| Q111ObsDR | - |  |  | SI | Capillary refill DR |
| Q113 | - |  |  | SI | Sensation |
| Q113N | - |  |  | SI | Note |
| Q113ObsDR | - |  |  | SI | Sensation DR |
| Q114 | - |  |  | SI | Weight bearing |
| Q114N | - |  |  | SI | Note |
| Q114ObsDR | - |  |  | SI | Weight bearing DR |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Distal sensation DR |
| Q12 | - |  |  | SI | Upper Arm/elbow |
| Q13 | - |  |  | SI | Range of motion |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Range of motion DR |
| Q14 | - |  |  | SI | Tenderness |
| Q14N | - |  |  | SI | Note |
| Q14ObsDR | - |  |  | SI | Tenderness DR |
| Q15 | - |  |  | SI | Deformity |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Deformity DR |
| Q16 | - |  |  | SI | Distal pulses |
| Q16N | - |  |  | SI | Note |
| Q16ObsDR | - |  |  | SI | Distal pulses DR |
| Q17 | - |  |  | SI | Distal sensation |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Distal sensation DR |
| Q18 | - |  |  | SI | Joint stability |
| Q18N | - |  |  | SI | Note |
| Q18ObsDR | - |  |  | SI | Joint stability DR |
| Q35 | - |  |  | SI | Forearm / wrist |
| Q36 | - |  |  | SI | Tenderness |
| Q36N | - |  |  | SI | Note |
| Q36ObsDR | - |  |  | SI | Tenderness DR |
| Q38 | - |  |  | SI | Range of motion |
| Q38N | - |  |  | SI | Note |
| Q38ObsDR | - |  |  | SI | Range of motion DR |
| Q40 | - |  |  | SI | Deformity |
| Q40N | - |  |  | SI | Note |
| Q40ObsDR | - |  |  | SI | Deformity DR |
| Q42 | - |  |  | SI | Distal pulses |
| Q42N | - |  |  | SI | Note |
| Q42ObsDR | - |  |  | SI | Distal pulses DR |
| Q43 | - |  |  | SI | Distal sensation |
| Q43N | - |  |  | SI | Note |
| Q43ObsDR | - |  |  | SI | Distal sensation DR |
| Q45 | - |  |  | SI | Joint stability |
| Q45N | - |  |  | SI | Note |
| Q45ObsDR | - |  |  | SI | Joint stability DR |
| Q48 | - |  |  | SI | Hand |
| Q49 | - |  |  | SI | Tenderness |
| Q49N | - |  |  | SI | Note |
| Q49ObsDR | - |  |  | SI | Tenderness DR |
| Q51 | - |  |  | SI | Range of motion |
| Q51N | - |  |  | SI | Note |
| Q51ObsDR | - |  |  | SI | Range of motion DR |
| Q53 | - |  |  | SI | Deformity |
| Q53N | - |  |  | SI | Note |
| Q53ObsDR | - |  |  | SI | Deformity DR |
| Q55 | - |  |  | SI | Capillary refill |
| Q55N | - |  |  | SI | Note |
| Q55ObsDR | - |  |  | SI | Capillary refill DR |
| Q57 | - |  |  | SI | Sensation |
| Q57N | - |  |  | SI | Note |
| Q57ObsDR | - |  |  | SI | Sensation DR |
| Q59 | - |  |  | SI | Two point discrimination |
| Q59N | - |  |  | SI | Note |
| Q59ObsDR | - |  |  | SI | Two point discrimination DR |
| Q61 | - |  |  | SI | Hip/femur |
| Q62 | - |  |  | SI | Tenderness |
| Q62N | - |  |  | SI | Note |
| Q62ObsDR | - |  |  | SI | Tenderness DR |
| Q64 | - |  |  | SI | Range of motion |
| Q64N | - |  |  | SI | Note |
| Q64ObsDR | - |  |  | SI | Range of motion DR |
| Q66 | - |  |  | SI | Deformity |
| Q66N | - |  |  | SI | Note |
| Q66ObsDR | - |  |  | SI | Deformity DR |
| Q68 | - |  |  | SI | Shortened |
| Q68N | - |  |  | SI | Note |
| Q68ObsDR | - |  |  | SI | Shortened DR |
| Q69 | - |  |  | SI | Externally Rotated |
| Q69N | - |  |  | SI | Note |
| Q69ObsDR | - |  |  | SI | Externally Rotated DR |
| Q70 | - |  |  | SI | Distal pulses |
| Q70N | - |  |  | SI | Note |
| Q70ObsDR | - |  |  | SI | Distal pulses DR |
| Q74 | - |  |  | SI | Distal sensation |
| Q74N | - |  |  | SI | Note |
| Q74ObsDR | - |  |  | SI | Distal sensation DR |
| Q75 | - |  |  | SI | Weight bearing |
| Q75N | - |  |  | SI | Note |
| Q75ObsDR | - |  |  | SI | Weight bearing DR |
| Q76 | - |  |  | SI | Knee |
| Q77 | - |  |  | SI | Tenderness |
| Q77N | - |  |  | SI | Note |
| Q77ObsDR | - |  |  | SI | Tenderness DR |
| Q79 | - |  |  | SI | Range of motion |
| Q79N | - |  |  | SI | Note |
| Q79ObsDR | - |  |  | SI | Range of motion DR |
| Q81 | - |  |  | SI | Deformity |
| Q81N | - |  |  | SI | Note |
| Q81ObsDR | - |  |  | SI | Deformity DR |
| Q83 | - |  |  | SI | Distal pulses |
| Q83N | - |  |  | SI | Note |
| Q83ObsDR | - |  |  | SI | Distal pulses DR |
| Q85 | - |  |  | SI | Distal sensation |
| Q85N | - |  |  | SI | Note |
| Q85ObsDR | - |  |  | SI | Distal sensation DR |
| Q87 | - |  |  | SI | Lachman test |
| Q87N | - |  |  | SI | Note |
| Q87ObsDR | - |  |  | SI | Lachman test DR |
| Q89 | - |  |  | SI | Joint stability |
| Q89N | - |  |  | SI | Note |
| Q89ObsDR | - |  |  | SI | Joint stability DR |
| Q90 | - |  |  | SI | Weight bearing |
| Q90N | - |  |  | SI | Note |
| Q90ObsDR | - |  |  | SI | Weight bearing DR |
| Q91 | - |  |  | SI | Lower leg/ankle |
| Q92 | - |  |  | SI | Tenderness |
| Q92N | - |  |  | SI | Note |
| Q92ObsDR | - |  |  | SI | Tenderness DR |
| Q94 | - |  |  | SI | Range of motion |
| Q94N | - |  |  | SI | Note |
| Q94ObsDR | - |  |  | SI | Range of motion DR |
| Q96 | - |  |  | SI | Deformity |
| Q96N | - |  |  | SI | Note |
| Q96ObsDR | - |  |  | SI | Deformity DR |
| Q98 | - |  |  | SI | Distal pulses |
| Q98N | - |  |  | SI | Note |
| Q98ObsDR | - |  |  | SI | Distal pulses DR |
| Q99 | - |  |  | SI | Weight bearing |
| Q99N | - |  |  | SI | Note |
| Q99ObsDR | - |  |  | SI | Weight bearing DR |
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