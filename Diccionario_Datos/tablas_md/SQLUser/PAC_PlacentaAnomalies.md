# SQLUser.PAC_PlacentaAnomalies

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLACANOM_RowId | bigint | PK |  | NO | - |
| PLACANOM_Active | varchar |  |  | SI | Active flag |
| PLACANOM_Code | varchar |  |  | NO | Code |
| PLACANOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLACANOM_CreatedDate | date |  |  | SI | Created Date |
| PLACANOM_CreatedTime | time |  |  | SI | Created Time |
| PLACANOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLACANOM_DateFrom | date |  |  | SI | Date From |
| PLACANOM_DateTo | date |  |  | SI | Date To |
| PLACANOM_Desc | varchar |  |  | NO | Description |
| PLACANOM_NationalCode | varchar |  |  | SI | National Code |
| PLACANOM_Owner | varchar |  |  | SI | Owner |
| PLACANOM_UpdatedDate | date |  |  | SI | Updated Date |
| PLACANOM_UpdatedTime | time |  |  | SI | Updated Time |
| PLACANOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Parity	 |
| Q04 | - |  |  | SI | Height |
| Q04A | - |  |  | SI | Reproductive history |
| Q04L | - |  |  | SI | Reproductive History |
| Q05 | - |  |  | SI | Body Mass Index (BMI)	 |
| Q05L | - |  |  | SI | Medical or Surgical Associated Conditions |
| Q06 | - |  |  | SI | 2 or more abortions or history of infertility	 |
| Q07 | - |  |  | SI | Postpartum bleeding or manual removal	 |
| Q08 | - |  |  | SI | Child > 4 kg	 |
| Q09 | - |  |  | SI | Child < 2.5 kg	 |
| Q10 | - |  |  | SI | Pre-term labour	 |
| Q11 | - |  |  | SI | Previous Cesarean Section	 |
| Q12 | - |  |  | SI | Forceps (low mid) / Vacuum	 |
| Q13 | - |  |  | SI | Breech	 |
| Q14 | - |  |  | SI | Perinatal death	 |
| Q15 | - |  |  | SI | Puerperal sepsis	 |
| Q16 | - |  |  | SI | Previous post-natal depression	 |
| Q17 | - |  |  | SI | Reproductive History Total	 |
| Q18 | - |  |  | SI | Previous gynaecological surgery	 |
| Q18A | - |  |  | SI | Medical or surgical associated conditions |
| Q19 | - |  |  | SI | Renal disease	 |
| Q20 | - |  |  | SI | Gestational diabetes on diet or oral hypoglycemics... |
| Q21 | - |  |  | SI | Diabetic on insulin	 |
| Q22 | - |  |  | SI | Cardiac disease	 |
| Q23 | - |  |  | SI | Asthma |
| Q24 | - |  |  | SI | Tuberculosis	 |
| Q25 | - |  |  | SI | Hypothyroidism	 |
| Q26 | - |  |  | SI | Other severe systemic infections	 |
| Q27 | - |  |  | SI | Hyperthyroidism	 |
| Q27A | - |  |  | SI | Hyperthyroidism |
| Q28 | - |  |  | SI | Epilepsy	 |
| Q28A | - |  |  | SI | Epilepsy |
| Q29 | - |  |  | SI | Syphilis |
| Q30 | - |  |  | SI | Bleeding disorder	 |
| Q31 | - |  |  | SI | Hepatitis |
| Q32 | - |  |  | SI | Group B streptococcus (GBS) positive	 |
| Q33 | - |  |  | SI | History of previous Venous thromboembolism (VTE)	 |
| Q34 | - |  |  | SI | Medical or Surgical Associated Conditions Total	 |
| Q34A | - |  |  | SI | Present pregnancy |
| Q35 | - |  |  | SI | Bleeding |
| Q35A | - |  |  | SI | Bleeding |
| Q35L | - |  |  | SI | Present Pregnancy |
| Q36 | - |  |  | SI | Anemia |
| Q37 | - |  |  | SI | Post maturity	 |
| Q38 | - |  |  | SI | Hypertension |
| Q39 | - |  |  | SI | Premature Rupture of Membranes (PROM)	 |
| Q40 | - |  |  | SI | Pre-labor premature rupture of membranes (PPROM)	 |
| Q41 | - |  |  | SI | Polyhydramnios |
| Q42 | - |  |  | SI | Oligohydramnios	 |
| Q43 | - |  |  | SI | Intrauterine growth restriction (IUGR)	 |
| Q44 | - |  |  | SI | Breech or mal-presentation	 |
| Q45 | - |  |  | SI | Multiple pregnancy	 |
| Q46 | - |  |  | SI | Rhesus (RH) isoimmunisation	 |
| Q47 | - |  |  | SI | Fibroids |
| Q48 | - |  |  | SI | Placenta previa	 |
| Q49 | - |  |  | SI | Present Pregnancy Total	 |
| Q50 | - |  |  | SI | Total Risk Score	 |
| Q51 | - |  |  | SI | 0-2 : Low Risk |
| Q52 | - |  |  | SI | 3-6 : High Risk |
| Q53 | - |  |  | SI | 7 or more : Severe Risk |
| Q54 | - |  |  | SI | All patients having a high or severe risk score ne... |
| Q55 | - |  |  | SI | This scoring tool is completed by the ObGyn doctor... |
| Q66 | - |  |  | SI | Date |
| Q67 | - |  |  | SI | Time |
| Q68 | - |  |  | SI | Reproductive History Total |
| Q69 | - |  |  | SI | Medical or Surgical Associated Conditions Total |
| Q70 | - |  |  | SI | Present Pregnancy Total |
| Q71 | - |  |  | SI | Total Risk Score |
| Q72 | - |  |  | SI | Other severe systemic infections |
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