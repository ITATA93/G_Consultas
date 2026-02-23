# SQLUser.PA_EnquiryContact

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENQ_RowId | bigint | PK |  | NO | - |
| ENQ_ActionDetails | varchar |  |  | SI | Action Details |
| ENQ_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ENQ_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| ENQ_CareProviderGroups | varchar |  |  | SI | CareProviderGroups  |
| ENQ_CityArea_DR | bigint |  | FK | SI | Des Ref CTCityArea |
| ENQ_City_DR | bigint |  | FK | SI | Des Ref CTCity |
| ENQ_ConsultCateg_DR | bigint |  | FK | SI | Des Ref OECConsultCateg |
| ENQ_ContClientPresStat_DR | bigint |  | FK | SI | Des Ref PACContClientPresStat |
| ENQ_ContDelivMode_DR | bigint |  | FK | SI | Des Ref PACContDelivMode |
| ENQ_ContDelivSetting_DR | bigint |  | FK | SI | Des Ref PACContDelivSetting |
| ENQ_ContInterpreterType_DR | bigint |  | FK | SI | Des Ref ContInterpreterType |
| ENQ_ContLocalGoal_DR | bigint |  | FK | SI | Des Ref ContLocalGoal |
| ENQ_ContMethod_DR | bigint |  | FK | SI | Des Ref ContMethod |
| ENQ_ContOutcome_DR | bigint |  | FK | SI | Des Ref ContOutcome |
| ENQ_ContServiceRec2_DR | bigint |  | FK | SI | Des Ref PACContServiceRec2  |
| ENQ_ContSessionType_DR | bigint |  | FK | SI | Des Ref PACContSessionType |
| ENQ_ContTimeBHR | varchar |  |  | SI | ContTimeBHR |
| ENQ_ContVenue_DR | bigint |  | FK | SI | Des Ref ContVenue |
| ENQ_ContWorkerType_DR | bigint |  | FK | SI | Des Ref ContWorkerType |
| ENQ_ContactInterventions | varchar |  |  | SI | ContactInterventions |
| ENQ_ContactName | varchar |  |  | SI | Contact Name |
| ENQ_ContactNumber | varchar |  |  | SI | Contact Number |
| ENQ_ContactType | varchar |  |  | SI | ContactType  |
| ENQ_Date | date |  |  | SI | Date |
| ENQ_DateUpdate | date |  |  | SI | Date Update |
| ENQ_DistanceTravelled | double |  |  | SI | DistanceTravelled |
| ENQ_Duration | double |  |  | SI | Duration |
| ENQ_EstimMins | double |  |  | SI | EstimMins |
| ENQ_EstimTime | time |  |  | SI | Estim Time |
| ENQ_Fee | double |  |  | SI | Fee |
| ENQ_GovernDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart |
| ENQ_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| ENQ_IndirectTime | double |  |  | SI | IndirectTime |
| ENQ_InpatientFlag | varchar |  |  | SI | InpatientFlag |
| ENQ_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ENQ_InterpreterRequired | varchar |  |  | SI | Interpreter Required |
| ENQ_InterpretingTime | double |  |  | SI | InterpretingTime |
| ENQ_ItemCat_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| ENQ_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| ENQ_NonGovOrg_DR | bigint |  | FK | SI | Des Ref NonGovOrg |
| ENQ_OEOrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ENQ_PAPER_DR | bigint |  | FK | SI | Des Ref PAPER |
| ENQ_Pictures_DR | varchar |  | FK | SI | Des Ref MRPictures |
| ENQ_RBEventTimes_DR | varchar |  | FK | SI | Des Ref RBEvent Session |
| ENQ_RBEvent_DR | bigint |  | FK | SI | Des Ref RBEvent |
| ENQ_ReqDesc | varchar |  |  | SI | Req Desc |
| ENQ_ReqReason | varchar |  |  | SI | Req Reason |
| ENQ_RequestStatus_DR | bigint |  | FK | SI | Des Ref RequestStatus |
| ENQ_RequestType_DR | bigint |  | FK | SI | Des Ref RequestType |
| ENQ_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| ENQ_ServiceTypeOutlet_DR | bigint |  | FK | SI | Service Type Outlet |
| ENQ_Sex_DR | bigint |  | FK | SI | Des Ref CTSex |
| ENQ_SourceOfReferral_DR | bigint |  | FK | SI | Des Ref SourceOfReferral |
| ENQ_Text1 | varchar |  |  | SI | Text1 |
| ENQ_Text2 | varchar |  |  | SI | Text2 |
| ENQ_Text3 | varchar |  |  | SI | Text3 |
| ENQ_Text4 | varchar |  |  | SI | Text4 |
| ENQ_Time | time |  |  | SI | Time |
| ENQ_TimeUpdate | time |  |  | SI | Time Update |
| ENQ_TravelTime | double |  |  | SI | TravelTime |
| ENQ_UrgentContact | varchar |  |  | SI | UrgentContact |
| ENQ_User_DR | bigint |  | FK | SI | Des Ref User |
| ENQ_VarianceReasonText | varchar |  |  | SI | VarianceReasonText |
| ENQ_VarianceReason_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason |
| ENQ_VolunteerSer | varchar |  |  | SI | VolunteerSer  |
| ENQ_WaitingList_DR | bigint |  | FK | SI | WaitingList |
| ENQ_YesNo1 | varchar |  |  | SI | YesNo1 |
| ENQ_YesNo2 | varchar |  |  | SI | YesNo2 |
| ENQ_YesNo3 | varchar |  |  | SI | YesNo3 |
| ENQ_YesNo4 | varchar |  |  | SI | YesNo4 |
| Q01 | - |  |  | SI | INTENSIDAD Y DURACIÓN DE LA PRESIÓN |
| Q03 | - |  |  | SI | Movilidad: Capacidad para cambiar y controlar la p... |
| Q04 | - |  |  | SI | Actividad: Nivel de actividad física |
| Q05 | - |  |  | SI | Percepción Sensorial: Capacidad de responder adecu... |
| Q06 | - |  |  | SI | TOLERANCIA DE LA PIEL Y LA ESTRUCTURA DE SOPORTE |
| Q07 | - |  |  | SI | Humedad: Nivel de exposición de la piel a la humed... |
| Q08 | - |  |  | SI | Fricción y Cizallamiento Fricción: Ocurre cuando l... |
| Q09 | - |  |  | SI | Nutrición: Patrón habitual de ingesta de alimentos... |
| Q10 | - |  |  | SI | Perfusión tisular y oxigenación |
| Q11 | - |  |  | SI | Comentarios |
| Q22 | - |  |  | SI | Fecha Evaluación |
| Q23 | - |  |  | SI | Hora Evaluación |
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