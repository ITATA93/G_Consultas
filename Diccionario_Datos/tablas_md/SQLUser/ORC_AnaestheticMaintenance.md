# SQLUser.ORC_AnaestheticMaintenance

**Schema:** SQLUser
**Columnas:** 205
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAMAI_RowId | bigint | PK |  | NO | - |
| ANAMAI_Code | varchar |  |  | NO | Code |
| ANAMAI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANAMAI_CreatedDate | date |  |  | SI | Created Date |
| ANAMAI_CreatedTime | time |  |  | SI | Created Time |
| ANAMAI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANAMAI_DateFrom | date |  |  | SI | Date From |
| ANAMAI_DateTo | date |  |  | SI | Date To |
| ANAMAI_Desc | varchar |  |  | NO | Description |
| ANAMAI_Owner | varchar |  |  | SI | Owner |
| ANAMAI_UpdatedDate | date |  |  | SI | Updated Date |
| ANAMAI_UpdatedTime | time |  |  | SI | Updated Time |
| ANAMAI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of Wheelchair Operated |
| Q02 | - |  |  | SI | Operates body positioning options |
| Q02N | - |  |  | SI | 02_Notes |
| Q02TG | - |  |  | SI | 02_Training Goal |
| Q03 | - |  |  | SI | Rolls forwards short distance |
| Q03N | - |  |  | SI | 03_Notes |
| Q03TG | - |  |  | SI | 03_Training Goal |
| Q04 | - |  |  | SI | Rolls backwards short distance |
| Q04N | - |  |  | SI | 04_Notes |
| Q04TG | - |  |  | SI | 04_Training Goal |
| Q05 | - |  |  | SI | Turns while moving forwards |
| Q05N | - |  |  | SI | 05_Notes |
| Q05TG | - |  |  | SI | 05_Training Goal |
| Q06 | - |  |  | SI | Turns while moving backwards |
| Q06N | - |  |  | SI | 06_Notes |
| Q06TG | - |  |  | SI | 06_Training Goal |
| Q07 | - |  |  | SI | Turns in place |
| Q07N | - |  |  | SI | 07_Notes |
| Q07TG | - |  |  | SI | 07_Training Goal |
| Q08 | - |  |  | SI | Manoeuvres sideways |
| Q08N | - |  |  | SI | 08_Notes |
| Q08TG | - |  |  | SI | 08_Training Goal |
| Q09 | - |  |  | SI | Gets through hinged door |
| Q09N | - |  |  | SI | 09_Notes |
| Q09TG | - |  |  | SI | 09_Training Goal |
| Q10 | - |  |  | SI | Reaches high object |
| Q10TG | - |  |  | SI | 10_Training Goal |
| Q10n | - |  |  | SI | 10_Notes |
| Q11 | - |  |  | SI | Picks object up from floor |
| Q11N | - |  |  | SI | 11_Notes |
| Q11TG | - |  |  | SI | 11_Training Goal |
| Q12 | - |  |  | SI | Relieves weight from buttocks |
| Q12N | - |  |  | SI | 12_Notes |
| Q12TG | - |  |  | SI | 12_Training Goal |
| Q13 | - |  |  | SI | Level transfer |
| Q13N | - |  |  | SI | 13_Notes |
| Q13TG | - |  |  | SI | 13_Training Goal |
| Q14 | - |  |  | SI | Folds and unfolds wheelchair |
| Q147 | - |  |  | SI | Individual Skill |
| Q148 | - |  |  | SI | Capacity Score |
| Q149 | - |  |  | SI | Training Goal |
| Q14N | - |  |  | SI | 14_Notes |
| Q14TG | - |  |  | SI | 14_Training Goal |
| Q15 | - |  |  | SI | Rolls longer distance |
| Q150 | - |  |  | SI | Notes |
| Q151 | - |  |  | SI | Total Capacity Score (Manual) |
| Q152 | - |  |  | SI | Total Capacity Score (Powered) |
| Q15N | - |  |  | SI | 15_Notes |
| Q15TG | - |  |  | SI | 15_Training Goal |
| Q16 | - |  |  | SI | Avoids moving obstacles |
| Q16N | - |  |  | SI | 16_Notes |
| Q16TG | - |  |  | SI | 16_Training Goal |
| Q17 | - |  |  | SI | Ascends steep incline |
| Q17N | - |  |  | SI | 17_Notes |
| Q17TG | - |  |  | SI | 17_Training Goal |
| Q18 | - |  |  | SI | Descends steep incline |
| Q18N | - |  |  | SI | 18_Notes |
| Q18TG | - |  |  | SI | 18_Training Goal |
| Q19 | - |  |  | SI | Ascends slight incline |
| Q19N | - |  |  | SI | 19_Notes |
| Q19TG | - |  |  | SI | 19_Training Goal |
| Q20 | - |  |  | SI | Descends slight incline |
| Q20N | - |  |  | SI | 20_Notes |
| Q20TG | - |  |  | SI | 20_Training Goal |
| Q21 | - |  |  | SI | Rolls across side-slope |
| Q21N | - |  |  | SI | 21_Notes |
| Q21TG | - |  |  | SI | 21_Training Goal |
| Q22 | - |  |  | SI | Rolls on soft surface |
| Q22N | - |  |  | SI | 22_Notes |
| Q22TG | - |  |  | SI | 22_Training Goal |
| Q23 | - |  |  | SI | Gets over threshold |
| Q23N | - |  |  | SI | 23_Notes |
| Q23TG | - |  |  | SI | 23_Training Goal |
| Q24 | - |  |  | SI | Gets over gap |
| Q24N | - |  |  | SI | 24_Notes |
| Q24TG | - |  |  | SI | 24_Training Goal |
| Q25 | - |  |  | SI | Ascends low curb |
| Q25N | - |  |  | SI | 25_Notes |
| Q25TG | - |  |  | SI | 25_Training Goal |
| Q26 | - |  |  | SI | Descends low curb |
| Q26N | - |  |  | SI | 26_Notes |
| Q26TG | - |  |  | SI | 26_Training Goal |
| Q27 | - |  |  | SI | Ascends high curb |
| Q27N | - |  |  | SI | 27_Notes |
| Q27TG | - |  |  | SI | 27_Training Goal |
| Q28 | - |  |  | SI | Descends high curb |
| Q28N | - |  |  | SI | 28_Notes |
| Q28TG | - |  |  | SI | 28_Training Goal |
| Q29 | - |  |  | SI | Performs stationary wheelie |
| Q29N | - |  |  | SI | 29_Notes |
| Q29TG | - |  |  | SI | 29_Training Goal |
| Q30 | - |  |  | SI | Turns in place in wheelie position |
| Q30N | - |  |  | SI | 30_Notes |
| Q30TG | - |  |  | SI | 30_Training Goal |
| Q31 | - |  |  | SI | Descends steep incline in wheelie position |
| Q31N | - |  |  | SI | 31_Notes |
| Q31TG | - |  |  | SI | 31_Training Goal |
| Q32 | - |  |  | SI | Descends high curb in wheelie position |
| Q32N | - |  |  | SI | 32_Notes |
| Q32TG | - |  |  | SI | 32_Training Goal |
| Q33 | - |  |  | SI | Gets from  ground into wheelchair |
| Q33N | - |  |  | SI | 33_Notes |
| Q33TG | - |  |  | SI | 33_Training Goal |
| Q34 | - |  |  | SI | Ascends stairs |
| Q34N | - |  |  | SI | 34_Notes |
| Q34TG | - |  |  | SI | 34_Training Goal |
| Q35 | - |  |  | SI | Descends stairs |
| Q35N | - |  |  | SI | 35_Notes |
| Q35TG | - |  |  | SI | 35_Training Goal |
| Q36 | - |  |  | SI | Moves controller away and back |
| Q36N | - |  |  | SI | 36_Notes |
| Q36TG | - |  |  | SI | 36_Training Goal |
| Q37 | - |  |  | SI | Turns power on and off |
| Q37N | - |  |  | SI | 37_Notes |
| Q37TG | - |  |  | SI | 37_Training Goal |
| Q38 | - |  |  | SI | Selects drive modes and speeds |
| Q38N | - |  |  | SI | 38_Notes |
| Q38TG | - |  |  | SI | 38_Training Goal |
| Q39 | - |  |  | SI | Disengages and engages motors |
| Q39N | - |  |  | SI | 39_Notes |
| Q39TG | - |  |  | SI | 39_Training Goal |
| Q40 | - |  |  | SI | Operates battery charger |
| Q40N | - |  |  | SI | 40_Notes |
| Q40TG | - |  |  | SI | 40_Training Goal |
| Q41 | - |  |  | SI | Total score (Manual) |
| Q42 | - |  |  | SI | Total score (Powered) |
| Q43 | - |  |  | SI | % |
| Q44 | - |  |  | SI | Comments |
| Q45 | - |  |  | SI | Training goals |
| Q46 | - |  |  | SI | WST 4.3 Form for Manual and Powered Wheelchairs Op... |
| Q47 | - |  |  | SI | Originally approved for distribution and use: Nove... |
| Q48 | - |  |  | SI | Copies can be downloaded from www.wheelchairskills... |
| Q49 | - |  |  | SI | Pass |
| Q50 | - |  |  | SI | Pass with difficulty |
| Q51 | - |  |  | SI | Fail |
| Q52 | - |  |  | SI | Not possible |
| Q53 | - |  |  | SI | Testing error |
| Q54 | - |  |  | SI | Task independently and safely accomplished without... |
| Q55 | - |  |  | SI | The evaluation criteria are met, but the subject e... |
| Q56 | - |  |  | SI | Task incomplete or unsafe |
| Q57 | - |  |  | SI | Wheelchair does not allow this skill (Only for ski... |
| Q58 | - |  |  | SI | Testing of the skill was not sufficiently well obs... |
| Q59 | - |  |  | SI | 2 |
| Q60 | - |  |  | SI | 1 |
| Q61 | - |  |  | SI | 0 |
| Q62 | - |  |  | SI | NP |
| Q63 | - |  |  | SI | TE |
| Q64 | - |  |  | SI | What this means |
| Q65 | - |  |  | SI | Score |
| Q66 | - |  |  | SI | Formula for Calculating Total Scores |
| Q67 | - |  |  | SI | Total Capacity Score (Manual) = sum of individual ... |
| Q68 | - |  |  | SI | Total Capacity Score  (Powered)= sum of individual... |
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