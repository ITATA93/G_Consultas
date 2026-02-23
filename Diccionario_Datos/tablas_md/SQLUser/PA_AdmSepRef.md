# SQLUser.PA_AdmSepRef

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEPREF_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Anaesthetic assessment completed |
| Q04 | - |  |  | SI | Variance |
| Q05 | - |  |  | SI | Patient's understanding of procedure confirmed and... |
| Q06 | - |  |  | SI | Variance |
| Q07 | - |  |  | SI | Baseline vital signs and neurovascular observation... |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Baseline height and weight recorded |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | 12 lead electrocardiogram performed and reviewed |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Patient received radiology request form |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | Patient received pathology request form |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Ordered blood tests completed and reviewed |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | Arranged for cross match two days prior to admissi... |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Skin assessed for wounds or fungal infection |
| Q22 | - |  |  | SI | Variance |
| Q23 | - |  |  | SI | Methicillin - resistant staphylococcus aureus (MRS... |
| Q24 | - |  |  | SI | Variance |
| Q25 | - |  |  | SI | Decolonisation information pamphlet provided and e... |
| Q26 | - |  |  | SI | Variance |
| Q27 | - |  |  | SI | Topical antibiotic given and use-of explained |
| Q28 | - |  |  | SI | Variance |
| Q29 | - |  |  | SI | Education provided for pre-operative washes and pr... |
| Q30 | - |  |  | SI | Variance |
| Q31 | - |  |  | SI | Patient provided with information brochure / watch... |
| Q32 | - |  |  | SI | Variance |
| Q33 | - |  |  | SI | Fasting requirements explained |
| Q34 | - |  |  | SI | Variance |
| Q35 | - |  |  | SI | Potential infection risks discussed |
| Q36 | - |  |  | SI | Examples: wounds, urinary tract and chest infectio... |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Length of stay discussed |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Enoxaparin administration discussed |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Referrals to allied health services organised as n... |
| Q43 | - |  |  | SI | Other referrals |
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
| SEPREF_Childsub | double |  |  | NO | Childsub |
| SEPREF_RowId | varchar |  |  | NO | - |
| SEPREF_SepRef_DR | bigint |  | FK | SI | Des Ref SepRef |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*