# questionnaire.QTCORA

> "Obstetric Risk Assessment	"

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Obstetric Risk Assessment	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age |
| Q02 | varchar |  |  | SI | Parity	 |
| Q04 | varchar |  |  | SI | Height |
| Q04A | varchar |  |  | SI | Reproductive history |
| Q04L | varchar |  |  | SI | Reproductive History |
| Q05 | varchar |  |  | SI | Body Mass Index (BMI)	 |
| Q05L | varchar |  |  | SI | Medical or Surgical Associated Conditions |
| Q06 | varchar |  |  | SI | 2 or more abortions or history of infertility	 |
| Q07 | varchar |  |  | SI | Postpartum bleeding or manual removal	 |
| Q08 | varchar |  |  | SI | Child > 4 kg	 |
| Q09 | varchar |  |  | SI | Child < 2.5 kg	 |
| Q10 | varchar |  |  | SI | Pre-term labour	 |
| Q11 | varchar |  |  | SI | Previous Cesarean Section	 |
| Q12 | varchar |  |  | SI | Forceps (low mid) / Vacuum	 |
| Q13 | varchar |  |  | SI | Breech	 |
| Q14 | varchar |  |  | SI | Perinatal death	 |
| Q15 | varchar |  |  | SI | Puerperal sepsis	 |
| Q16 | varchar |  |  | SI | Previous post-natal depression	 |
| Q17 | varchar |  |  | SI | Reproductive History Total	 |
| Q18 | varchar |  |  | SI | Previous gynaecological surgery	 |
| Q18A | varchar |  |  | SI | Medical or surgical associated conditions |
| Q19 | varchar |  |  | SI | Renal disease	 |
| Q20 | varchar |  |  | SI | Gestational diabetes on diet or oral hypoglycemics... |
| Q21 | varchar |  |  | SI | Diabetic on insulin	 |
| Q22 | varchar |  |  | SI | Cardiac disease	 |
| Q23 | varchar |  |  | SI | Asthma |
| Q24 | varchar |  |  | SI | Tuberculosis	 |
| Q25 | varchar |  |  | SI | Hypothyroidism	 |
| Q26 | varchar |  |  | SI | Other severe systemic infections	 |
| Q27 | varchar |  |  | SI | Hyperthyroidism	 |
| Q27A | varchar |  |  | SI | Hyperthyroidism |
| Q28 | varchar |  |  | SI | Epilepsy	 |
| Q28A | varchar |  |  | SI | Epilepsy |
| Q29 | varchar |  |  | SI | Syphilis |
| Q30 | varchar |  |  | SI | Bleeding disorder	 |
| Q31 | varchar |  |  | SI | Hepatitis |
| Q32 | varchar |  |  | SI | Group B streptococcus (GBS) positive	 |
| Q33 | varchar |  |  | SI | History of previous Venous thromboembolism (VTE)	 |
| Q34 | varchar |  |  | SI | Medical or Surgical Associated Conditions Total	 |
| Q34A | varchar |  |  | SI | Present pregnancy |
| Q35 | varchar |  |  | SI | Bleeding |
| Q35A | varchar |  |  | SI | Bleeding |
| Q35L | varchar |  |  | SI | Present Pregnancy |
| Q36 | varchar |  |  | SI | Anemia |
| Q37 | varchar |  |  | SI | Post maturity	 |
| Q38 | varchar |  |  | SI | Hypertension |
| Q39 | varchar |  |  | SI | Premature Rupture of Membranes (PROM)	 |
| Q40 | varchar |  |  | SI | Pre-labor premature rupture of membranes (PPROM)	 |
| Q41 | varchar |  |  | SI | Polyhydramnios |
| Q42 | varchar |  |  | SI | Oligohydramnios	 |
| Q43 | varchar |  |  | SI | Intrauterine growth restriction (IUGR)	 |
| Q44 | varchar |  |  | SI | Breech or mal-presentation	 |
| Q45 | varchar |  |  | SI | Multiple pregnancy	 |
| Q46 | varchar |  |  | SI | Rhesus (RH) isoimmunisation	 |
| Q47 | varchar |  |  | SI | Fibroids |
| Q48 | varchar |  |  | SI | Placenta previa	 |
| Q49 | varchar |  |  | SI | Present Pregnancy Total	 |
| Q50 | varchar |  |  | SI | Total Risk Score	 |
| Q51 | varchar |  |  | SI | 0-2 : Low Risk |
| Q52 | varchar |  |  | SI | 3-6 : High Risk |
| Q53 | varchar |  |  | SI | 7 or more : Severe Risk |
| Q54 | varchar |  |  | SI | All patients having a high or severe risk score ne... |
| Q55 | varchar |  |  | SI | This scoring tool is completed by the ObGyn doctor... |
| Q66 | date |  |  | SI | Date |
| Q67 | time |  |  | SI | Time |
| Q68 | varchar |  |  | SI | Reproductive History Total |
| Q69 | varchar |  |  | SI | Medical or Surgical Associated Conditions Total |
| Q70 | varchar |  |  | SI | Present Pregnancy Total |
| Q71 | varchar |  |  | SI | Total Risk Score |
| Q72 | varchar |  |  | SI | Other severe systemic infections |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*