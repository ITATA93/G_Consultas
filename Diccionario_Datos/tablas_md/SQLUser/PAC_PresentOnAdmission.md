# SQLUser.PAC_PresentOnAdmission

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESADM_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Wound site 	 |
| PRESADM_Code | varchar |  |  | NO | Code |
| PRESADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRESADM_CreatedDate | date |  |  | SI | Created Date |
| PRESADM_CreatedTime | time |  |  | SI | Created Time |
| PRESADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRESADM_DateFrom | date |  |  | SI | Date From |
| PRESADM_DateTo | date |  |  | SI | Date To |
| PRESADM_Desc | varchar |  |  | NO | Description |
| PRESADM_Owner | varchar |  |  | SI | Owner |
| PRESADM_UpdatedDate | date |  |  | SI | Updated Date |
| PRESADM_UpdatedTime | time |  |  | SI | Updated Time |
| PRESADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure name |
| Q02 | - |  |  | SI | Recovery date 	 |
| Q03 | - |  |  | SI | Recovery time	 |
| Q04 | - |  |  | SI | Recovery practitioner 	 |
| Q05 | - |  |  | SI | Airway support 	 |
| Q05ObsDR | - |  |  | SI | Airway support 	 DR |
| Q06 | - |  |  | SI | Extubated / airway expelled 	 |
| Q07 | - |  |  | SI | O2 Delivery mode 	 |
| Q07ObsDR | - |  |  | SI | O2 Delivery mode 	 DR |
| Q08 | - |  |  | SI | Oxygen administered %	 |
| Q08ObsDR | - |  |  | SI | Oxygen administered %	 DR |
| Q09 | - |  |  | SI | Oxygen flow (L)	 |
| Q09ObsDR | - |  |  | SI | Oxygen flow (L)	 DR |
| Q10 | - |  |  | SI | Oxygen duration (hh:mm)	 |
| Q12 | - |  |  | SI | PV loss	 |
| Q12ObsDR | - |  |  | SI | PV loss	 DR |
| Q13 | - |  |  | SI | Skin condition	 |
| Q13ObsDR | - |  |  | SI | Skin condition	 DR |
| Q14 | - |  |  | SI | Number of drains 	 |
| Q15 | - |  |  | SI | Nasogastric tube 	 |
| Q16 | - |  |  | SI | Vacuum drain	 |
| Q17 | - |  |  | SI | Urinary catheter 	 |
| Q19 | - |  |  | SI | Analgesia used	 |
| Q20 | - |  |  | SI | Specify 	 |
| Q21 | - |  |  | SI | Assessment on admission 	 |
| Q22 | - |  |  | SI | Arterial used	 |
| Q23 | - |  |  | SI | Central used	 |
| Q24 | - |  |  | SI | Anaesthesia discussed	 |
| Q25 | - |  |  | SI | Relevant medical history	 |
| Q26 | - |  |  | SI | Analgesia discussed	 |
| Q27 | - |  |  | SI | Medication discussed	 |
| Q28 | - |  |  | SI | Oxygen therapy discussed	 |
| Q29 | - |  |  | SI | I.V. Fluids discussed	 |
| Q30 | - |  |  | SI | VIAD chart commenced 	 |
| Q31 | - |  |  | SI | Additional information 	 |
| Q32 | - |  |  | SI | Anaesthetic handover	 |
| Q33 | - |  |  | SI | Recovery practitioner 	 |
| Q34 | - |  |  | SI | The following items have been discussed 	 |
| Q35 | - |  |  | SI | Procedure discussed	 |
| Q36 | - |  |  | SI | Skin integrity checked 	 |
| Q37 | - |  |  | SI | Specify |
| Q38 | - |  |  | SI | Dressings	 |
| Q39 | - |  |  | SI | Drains	 |
| Q40 | - |  |  | SI | Catheters	 |
| Q41 | - |  |  | SI | Analgesia / blocks	 |
| Q42 | - |  |  | SI | Complications	 |
| Q43 | - |  |  | SI | Blood loss	 |
| Q44 | - |  |  | SI | Allergies	 |
| Q45 | - |  |  | SI | Additional information	 |
| Q46 | - |  |  | SI | Theatre practitioner 	 |
| Q47 | - |  |  | SI | Recovery practitioner 	 |
| Q48 | - |  |  | SI | Post operative plan 	 |
| Q49 | - |  |  | SI | Additional information 	 |
| Q50 | - |  |  | SI | Surgical handover	 |
| Q51 | - |  |  | SI | Recovery practitioner	 |
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