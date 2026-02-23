# SQLUser.PA_AdmTransaction

**Schema:** SQLUser
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANS_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Post-op day |
| Q04 | - |  |  | SI | Alert and oriented |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Patient monitored and assessed for delirium |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Patient provided education on using patient-contro... |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | All medication administered as ordered |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Intravenous fluid therapy administered as ordered |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Chest physiotherapy encouraged as clinically indic... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Patient is receiving appropriate venous thrombus p... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Patient provided education and demonstrated how to... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Patient supervised in the self administration of e... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | All ordered investigations / tests taken and resul... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Episodes of nausea and vomiting are effectively co... |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Patient is tolerating oral fluids and diet |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Strict fluid balance chart maintained |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | All bowel motions documented |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Drain remained patent and all drainage documented.... |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Drain removed as ordered with no complications |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Patient skin integrity assessed and free from pres... |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Patient has received regular pressure area care wi... |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Pressure relieving devices in situ as needed |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Personal hygiene attended |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Patient received mouth care as clinically indicate... |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Patient mobilised with assistance from physiothera... |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Knee immobiliser fitted and comfortable |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | Knee brace in situ |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Patient is tolerating continuous passive movement |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Patient has stood / sat out of bed |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | All interventions explained to patient / family |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Patient provided orientation to ward if required |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | Patient safety considered (i.e. bedside rails, pat... |
| Q73 | - |  |  | SI | Variance |
| Q74 | - |  |  | SI | Patient reviewed by the occupational therapist for... |
| Q75 | - |  |  | SI | Variance |
| Q76 | - |  |  | SI | Referrals arranged as necessary |
| Q77 | - |  |  | SI | Variance |
| Q78 | - |  |  | SI | Commence discharge planning |
| Q79 | - |  |  | SI | Variance |
| Q80 | - |  |  | SI | Continue discharge planning |
| Q81 | - |  |  | SI | Variance |
| Q82 | - |  |  | SI | Discharge planning includes: |
| Q83 | - |  |  | SI | • Outpatient appointment booked |
| Q84 | - |  |  | SI | • Plan for suture removal if required |
| Q85 | - |  |  | SI | • Enoxaparin information pack provided to patient |
| Q86 | - |  |  | SI | • Community referral for enoxaparin administration... |
| Q87 | - |  |  | SI | • Equipment is ready for discharge |
| Q88 | - |  |  | SI | • Discharge medications ordered |
| Q89 | - |  |  | SI | • Patient able to achieve 90º flexion prior to dis... |
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
| TRANS_AccomodationType_DR | bigint |  | FK | SI | Des Ref AccomodationType |
| TRANS_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| TRANS_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| TRANS_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| TRANS_BedType_DR | bigint |  | FK | SI | Des Ref BedType |
| TRANS_Bed_DR | varchar |  | FK | SI | Des Ref Bed |
| TRANS_CTCP_DR | varchar |  | FK | SI | Des Ref to CTCP |
| TRANS_CTLOC_DR | bigint |  | FK | SI | Des REf CTLOC |
| TRANS_Childsub | double |  |  | NO | Childsub |
| TRANS_Closure | varchar |  |  | SI | Closure |
| TRANS_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| TRANS_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| TRANS_CreateDate | date |  |  | SI | Create Date |
| TRANS_CreateTime | time |  |  | SI | Create Time |
| TRANS_CreateUser_DR | bigint |  | FK | SI | Des Ref CreateUser |
| TRANS_DRG_DR | bigint |  | FK | SI | Des Ref TRANS_DRG_DR |
| TRANS_DateAccepted | date |  |  | SI | Date Accepted |
| TRANS_Dept_DR | bigint |  | FK | SI | Des Ref CTLOC |
| TRANS_EmbDayCase | varchar |  |  | SI | EmbDayCase |
| TRANS_EmergConsultant_DR | varchar |  | FK | SI | Des Ref Emergency Consultant |
| TRANS_EndDate | date |  |  | SI | End Date |
| TRANS_EndTime | time |  |  | SI | End Time |
| TRANS_ExpBedLengthOfStay | double |  |  | SI | Expected Bed Length Of Stay  |
| TRANS_ExpBedLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| TRANS_ExpLengthOfStay | double |  |  | SI | Expected Length Of Stay  |
| TRANS_ExpLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| TRANS_ExpectedBedOutDate | date |  |  | SI | Expected Bed Out Date |
| TRANS_ExpectedBedOutTime | time |  |  | SI | Expected Bed Out Time |
| TRANS_ExpectedBedVacancy | date |  |  | SI | ExpectedBedVacancy |
| TRANS_HRG_DR | bigint |  | FK | SI | Des Ref HRG |
| TRANS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TRANS_ICUBedRequired | varchar |  |  | SI | ICU Bed Required |
| TRANS_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| TRANS_IsolationRequired | varchar |  |  | SI | Isolation Required |
| TRANS_KeepOnDischarge | varchar |  |  | SI | TRANSKeepOnDischarge |
| TRANS_LikelihoodAdmit | varchar |  |  | SI | Likelihood to Admit
Put onto the Transaction as w... |
| TRANS_LinkedMovement_DR | varchar |  | FK | SI | Des Ref Linked Movement |
| TRANS_Main | varchar |  |  | SI | Main |
| TRANS_MoveMROnDischarge | varchar |  |  | SI | MoveMROnDischarge |
| TRANS_OnMedicalGrounds | varchar |  |  | SI | OnMedicalGrounds |
| TRANS_OverrideRoomType_DR | bigint |  | FK | SI | Des Ref OverrideRoomType |
| TRANS_PayByResult | varchar |  |  | SI | Payment By Result |
| TRANS_PostOpBedRequest | varchar |  |  | SI | Post Operative Bed Request |
| TRANS_RMCCareProv_DR | varchar |  | FK | SI | Rapid Management Clinician, des ref CTCareProv |
| TRANS_ReadyForBill | varchar |  |  | SI | ReadyForBill |
| TRANS_Reason_DR | bigint |  | FK | SI | Des Ref BedTransfer_Reason |
| TRANS_RejectReason_DR | bigint |  | FK | SI | Des Ref PACTransRejectReason |
| TRANS_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| TRANS_RoomType_DR | bigint |  | FK | SI | Des Ref PAC RoomType |
| TRANS_Room_DR | bigint |  | FK | SI | Des Ref to Room |
| TRANS_RowId | varchar |  |  | NO | - |
| TRANS_StartDate | date |  |  | SI | Start Date |
| TRANS_StartTime | time |  |  | SI | Start Time |
| TRANS_Status_DR | bigint |  | FK | SI | Des Ref PACTransfReqStatus |
| TRANS_TembTempLoc | varchar |  |  | SI | TembTempLoc |
| TRANS_TempLocFreeText | varchar |  |  | SI | TempLocFreeText |
| TRANS_TempLoc_DR | bigint |  | FK | SI | Des REf CTLOC |
| TRANS_TimeAccepted | time |  |  | SI | Time Accepted |
| TRANS_TransType_DR | bigint |  | FK | SI | Des Ref TransType |
| TRANS_TransferRemark | varchar |  |  | SI | TransferRemark |
| TRANS_UpdateDate | date |  |  | SI | Update Date |
| TRANS_UpdateTime | time |  |  | SI | Update Time |
| TRANS_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| TRANS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| TRANS_Verified | varchar |  |  | SI | Verified |
| TRANS_WardRoom_DR | varchar |  | FK | SI | Des Ref to PACWardRoom - To be used in web.Msg.PAA... |
| TRANS_Ward_DR | bigint |  | FK | SI | Des Ref to Ward |
| TRANS_Warned | varchar |  |  | SI | Warned |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*