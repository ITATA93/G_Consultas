# SQLUser.CT_RefClnContractDetails

**Schema:** SQLUser
**Columnas:** 165
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTR_ParRef | bigint | PK |  | NO | CT_RefClin Parent Reference |
| CONTR_CONTR_DR | bigint |  | FK | SI | Des REf CONTRact Det |
| CONTR_Childsub | double |  |  | NO | Childsub |
| CONTR_CreatedDate | date |  |  | SI | Created Date |
| CONTR_CreatedTime | time |  |  | SI | Created Time |
| CONTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTR_DateFrom | date |  |  | SI | Date From |
| CONTR_DateTo | date |  |  | SI | Date To |
| CONTR_RowId | varchar |  |  | NO | - |
| CONTR_UpdatedDate | date |  |  | SI | Updated Date |
| CONTR_UpdatedTime | time |  |  | SI | Updated Time |
| CONTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Name bands checked by parents |
| Q02 | - |  |  | SI | Temperature (°C) |
| Q02ObsDR | - |  |  | SI | Temperature (°C) DR |
| Q03 | - |  |  | SI | Heart rate&nbsp |
| Q03ObsDR | - |  |  | SI | Heart rate&nbsp |
| Q04 | - |  |  | SI | Respiratory rate&nbsp |
| Q04ObsDR | - |  |  | SI | Respiratory rate&nbsp |
| Q05 | - |  |  | SI | Weight |
| Q05ObsDR | - |  |  | SI | Weight DR |
| Q06 | - |  |  | SI | Length |
| Q06ObsDR | - |  |  | SI | Length DR |
| Q07 | - |  |  | SI | Head circumference |
| Q07ObsDR | - |  |  | SI | Head circumference DR |
| Q07a | - |  |  | SI | Neonatal head circumference&nbsp |
| Q07aObsDR | - |  |  | SI | Neonatal head circumference&nbsp |
| Q08 | - |  |  | SI | Consent to administer vitamin K&nbsp |
| Q08ObsDR | - |  |  | SI | Consent to administer vitamin K&nbsp |
| Q09 | - |  |  | SI | Has the paediatrician been contacted? |
| Q09ObsDR | - |  |  | SI | Has the paediatrician been contacted? DR |
| Q10 | - |  |  | SI | Vitamin K given by |
| Q11 | - |  |  | SI | Vitamin K checked by |
| Q12 | - |  |  | SI | Vitamin K batch no |
| Q12ObsDR | - |  |  | SI | Vitamin K batch no DR |
| Q13 | - |  |  | SI | Administration route |
| Q13ObsDR | - |  |  | SI | Administration route DR |
| Q14 | - |  |  | SI | Are the sagittal sutures &amp |
| Q14ObsDR | - |  |  | SI | Are the sagittal sutures &amp |
| Q15 | - |  |  | SI | Do the eyes appear normal? |
| Q15ObsDR | - |  |  | SI | Do the eyes appear normal? DR |
| Q16 | - |  |  | SI | Do the ears appear normal? |
| Q16ObsDR | - |  |  | SI | Do the ears appear normal? DR |
| Q17 | - |  |  | SI | Mouth & palate normal |
| Q17ObsDR | - |  |  | SI | Mouth & palate normal DR |
| Q18 | - |  |  | SI | Does the neck appear normal? |
| Q18ObsDR | - |  |  | SI | Does the neck appear normal? DR |
| Q19 | - |  |  | SI | Skin colour normal |
| Q19ObsDR | - |  |  | SI | Skin colour normal DR |
| Q20 | - |  |  | SI | Does the chest appear normal? |
| Q20ObsDR | - |  |  | SI | Does the chest appear normal? DR |
| Q21 | - |  |  | SI | Does the umbilical cord appear normal? |
| Q21ObsDR | - |  |  | SI | Does the umbilical cord appear normal? DR |
| Q22 | - |  |  | SI | Genitalia normal |
| Q22ObsDR | - |  |  | SI | Genitalia normal DR |
| Q23 | - |  |  | SI | Anus normal |
| Q23ObsDR | - |  |  | SI | Anus normal DR |
| Q24 | - |  |  | SI | Spine normal |
| Q24ObsDR | - |  |  | SI | Spine normal DR |
| Q25 | - |  |  | SI | Limb skin colour normal |
| Q25ObsDR | - |  |  | SI | Limb skin colour normal DR |
| Q26 | - |  |  | SI | Palmar / Plantar creases normal |
| Q26ObsDR | - |  |  | SI | Palmar / Plantar creases normal DR |
| Q27 | - |  |  | SI | Muscle tone normal |
| Q27ObsDR | - |  |  | SI | Muscle tone normal DR |
| Q28 | - |  |  | SI | Digits normal |
| Q28ObsDR | - |  |  | SI | Digits normal DR |
| Q29 | - |  |  | SI | Axillae normal |
| Q29ObsDR | - |  |  | SI | Axillae normal DR |
| Q30 | - |  |  | SI | Examination notes |
| Q31 | - |  |  | SI | Cord bloods sent for rhesus programme |
| Q31ObsDR | - |  |  | SI | Cord bloods sent for rhesus programme DR |
| Q32 | - |  |  | SI | Rhesus bloods sent - date |
| Q33 | - |  |  | SI | Rhesus bloods sent - time |
| Q34 | - |  |  | SI | Has the first feed&nbsp |
| Q34ObsDR | - |  |  | SI | Has the first feed&nbsp |
| Q35 | - |  |  | SI | First breastfeeding offered date |
| Q36 | - |  |  | SI | First artificial feeding offered date |
| Q37 | - |  |  | SI | First breastfeeding offered time |
| Q38 | - |  |  | SI | First artificial feeding offered time |
| Q39 | - |  |  | SI | Vitamin K oral dose |
| Q39ObsDR | - |  |  | SI | Vitamin K oral dose DR |
| Q40 | - |  |  | SI | Blood group +Rhesus |
| Q40ObsDR | - |  |  | SI | Blood group +Rhesus DR |
| Q41 | - |  |  | SI | Midwife countersigning |
| Q43 | - |  |  | SI | Blood group type and rhesus status |
| Q44 | - |  |  | SI | Date |
| Q45 | - |  |  | SI | Time |
| Q46 | - |  |  | SI | Have the baby's name bands been checked by parents... |
| Q47 | - |  |  | SI | Weight (kg) |
| Q47ObsDR | - |  |  | SI | Weight (kg) DR |
| Q48 | - |  |  | SI | Length (cm) |
| Q48ObsDR | - |  |  | SI | Length (cm) DR |
| Q49 | - |  |  | SI | Neonatal thoracic circumference (cm) |
| Q49ObsDR | - |  |  | SI | Neonatal thoracic circumference (cm) DR |
| Q50 | - |  |  | SI | Neonatal abdominal girth (cm) |
| Q50ObsDR | - |  |  | SI | Neonatal abdominal girth (cm) DR |
| Q51 | - |  |  | SI | Sutures &amp |
| Q52 | - |  |  | SI | Eyes comment |
| Q53 | - |  |  | SI | Mouth &amp |
| Q54 | - |  |  | SI | Neck comments |
| Q55 | - |  |  | SI | Skin colour comments |
| Q56 | - |  |  | SI | Limb skin colour comments |
| Q57 | - |  |  | SI | Digits comments |
| Q58 | - |  |  | SI | Chest comments |
| Q59 | - |  |  | SI | Umbilical cord comments |
| Q60 | - |  |  | SI | Genitalia comments |
| Q61 | - |  |  | SI | Anus comments |
| Q62 | - |  |  | SI | Spine&nbsp |
| Q63 | - |  |  | SI | Palmar / Plantar creases comments |
| Q64 | - |  |  | SI | Muscle tone comments |
| Q65 | - |  |  | SI | Reflexes comments |
| Q66 | - |  |  | SI | Axillae comments |
| Q67 | - |  |  | SI | Hips normal |
| Q68 | - |  |  | SI | Hips comments |
| Q69 | - |  |  | SI | Notes |
| Q70 | - |  |  | SI | Administering prophylactic eye treatment |
| Q71 | - |  |  | SI | Prophylactic eye treatment given by |
| Q72 | - |  |  | SI | Prophylactic eye treatment checked by |
| Q73 | - |  |  | SI | Type of prophylactic eye treatment |
| Q74 | - |  |  | SI | Administration route |
| Q75 | - |  |  | SI | Notes |
| Q76 | - |  |  | SI | Ears comment |
| Q77 | - |  |  | SI | Reflexes normal |
| Q77ObsDR | - |  |  | SI | Reflexes normal DR |
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