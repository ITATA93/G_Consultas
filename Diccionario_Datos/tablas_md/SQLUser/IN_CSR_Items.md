# SQLUser.IN_CSR_Items

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CSRI_ParRef | bigint | PK |  | NO | IN_CSR Parent Reference |
| CSRI_ChangeType | varchar |  |  | SI | ChangeType |
| CSRI_Childsub | double |  |  | NO | Childsub |
| CSRI_INCI_DR | bigint |  | FK | NO | Des Ref to INCI |
| CSRI_INCLB_DR_Laundry | varchar |  |  | SI | Des Ref to INCLB(Laundry) |
| CSRI_INCLB_DR_Ward | varchar |  |  | SI | Des Ref to INCLB(Ward) |
| CSRI_Qty_Changed | double |  |  | SI | Qty Changed |
| CSRI_Qty_Received | double |  |  | SI | Qty Received |
| CSRI_Qty_Requested | double |  |  | SI | Qty Requested |
| CSRI_Qty_Returned_Clean | double |  |  | SI | Qty Returned Clean |
| CSRI_Qty_Returned_Dirty | double |  |  | SI | Qty Returned Dirty |
| CSRI_Qty_in_Laundry | double |  |  | SI | Qty in Laundry |
| CSRI_Qty_in_Ward | double |  |  | SI | Qty_in_Ward |
| CSRI_Qty_in_Ward_Dirty | double |  |  | SI | Qty in Ward Dirty |
| CSRI_Remarks | varchar |  |  | SI | Remarks |
| CSRI_RowId | varchar |  |  | NO | - |
| CSRI_SterCat_DR | bigint |  | FK | SI | Des Ref to SterCat |
| Q01 | - |  |  | SI | Not at all |
| Q02 | - |  |  | SI | Very much so |
| Q03 | - |  |  | SI | Do you feel irritable? |
| Q04 | - |  |  | SI | Do you feel fatigued? |
| Q05 | - |  |  | SI | Do you feel tense? |
| Q06 | - |  |  | SI | Do you have difficulty concentrating? |
| Q07 | - |  |  | SI | Do you have any loss of appetite? |
| Q08 | - |  |  | SI | Have you any numbness or burning in your face, han... |
| Q09 | - |  |  | SI | Do you feel your heart racing (palpitations)? |
| Q10 | - |  |  | SI | Does your head feel full or achy? |
| Q11 | - |  |  | SI | Do you feel muscle aches or stiffness? |
| Q12 | - |  |  | SI | Do you feel anxious, nervous or jittery? |
| Q13 | - |  |  | SI | Do you feel upset? |
| Q14 | - |  |  | SI | How restful was your sleep last night? |
| Q15 | - |  |  | SI | Do you feel weak? |
| Q16 | - |  |  | SI | Do you think you had enough sleep last night? |
| Q17 | - |  |  | SI | Do you have any visual disturbances?(sensitivity t... |
| Q18 | - |  |  | SI | Are you fearful? |
| Q19 | - |  |  | SI | Have you been worrying about possible misfortunes ... |
| Q20 | - |  |  | SI | Observe behaviour for restlessness and agitation	 |
| Q21 | - |  |  | SI | Ask the patient to extend arms with fingers apart,... |
| Q22 | - |  |  | SI | Observe for sweating - feel palms	 |
| Q23 | - |  |  | SI | Total score	 |
| Q25 | - |  |  | SI | Alert, orientated, obeys commands? If NO, complete... |
| Q26 | - |  |  | SI | Pupil size left |
| Q26ObsDR | - |  |  | SI | Pupil size left DR |
| Q27 | - |  |  | SI | Pupil reaction left |
| Q27ObsDR | - |  |  | SI | Pupil reaction left DR |
| Q28 | - |  |  | SI | Pupil size right |
| Q28ObsDR | - |  |  | SI | Pupil size right DR |
| Q29 | - |  |  | SI | Pupil reaction right |
| Q29ObsDR | - |  |  | SI | Pupil reaction right DR |
| Q30 | - |  |  | SI | Score |
| Q31 | - |  |  | SI | Classification |
| Q32 | - |  |  | SI | 1-20 |
| Q33 | - |  |  | SI | Mild withdrawal |
| Q34 | - |  |  | SI | 21-40 |
| Q35 | - |  |  | SI | Moderate withdrawal |
| Q36 | - |  |  | SI | 41-60 |
| Q37 | - |  |  | SI | Severe withdrawal |
| Q38 | - |  |  | SI | 61-80 |
| Q39 | - |  |  | SI | Very severe withdrawal |
| Q40 | - |  |  | SI | The Benzodiazepine Withdrawal Scale is used to ass... |
| Q41 | - |  |  | SI | 0 |
| Q42 | - |  |  | SI | No signs of withdrawal |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time |
| Q45 | - |  |  | SI | Clinician to ask patient the following questions a... |
| Q46 | - |  |  | SI | How many hours of sleep do you think you had last ... |
| Q47 | - |  |  | SI | How many minutes do you think it took you to fall ... |
| Q48 | - |  |  | SI | The 'Clinical Institute Withdrawal Scale - Benzodi... |
| Q49 | - |  |  | SI | Hulse G, O’Neil G, Morris N, et al. Withdrawal and... |
| Q50 | - |  |  | SI | J Psychopharmacol&nbsp |
| Q51 | - |  |  | SI | Busto UE, Sykora K, Sellers EM. A clinical scale t... |
| Q52 | - |  |  | SI | Vital signs observation chart is required when com... |
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