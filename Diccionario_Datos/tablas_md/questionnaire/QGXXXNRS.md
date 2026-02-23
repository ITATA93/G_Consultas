# questionnaire.QGXXXNRS

**Schema:** questionnaire
**Columnas:** 193
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Walking |
| Q01N | varchar | PK |  | SI | Note |
| Q01ObsDR | varchar | PK | FK | SI | Walking DR |
| Q03 | varchar | PK |  | SI | Automatic movements |
| Q03N | varchar | PK |  | SI | Note |
| Q03ObsDR | varchar | PK | FK | SI | Automatic movements DR |
| Q05 | varchar | PK |  | SI | Upright position |
| Q05N | varchar | PK |  | SI | Note |
| Q05ObsDR | varchar | PK | FK | SI | Upright position DR |
| Q07 | varchar | PK |  | SI | Romberg Test |
| Q07N | varchar | PK |  | SI | Note |
| Q07ObsDR | varchar | PK | FK | SI | Romberg Test DR |
| Q09 | varchar | PK |  | SI | Passive motility |
| Q09N | varchar | PK |  | SI | Note |
| Q09ObsDR | varchar | PK | FK | SI | Passive motility DR |
| Q101 | varchar | PK |  | SI | XII Nervus hypoglossus |
| Q101N | varchar | PK |  | SI | Note |
| Q101ObsDR | varchar | PK | FK | SI | XII Nervus hypoglossus DR |
| Q103 | varchar | PK |  | SI | Upon arrival in the ED |
| Q104 | varchar | PK |  | SI | Admission at Stroke Unit |
| Q105 | varchar | PK |  | SI | Discharge from Stroke Unit |
| Q106 | varchar | PK |  | SI | Pre stroke |
| Q107 | varchar | PK |  | SI | Admission |
| Q108 | varchar | PK |  | SI | Discharge |
| Q109 | varchar | PK |  | SI | Reflexes muscularis |
| Q109N | varchar | PK |  | SI | Note |
| Q109ObsDR | varchar | PK | FK | SI | Reflexes muscularis DR |
| Q11 | varchar | PK |  | SI | Active motility and muscle strength |
| Q11N | varchar | PK |  | SI | Note |
| Q11ObsDR | varchar | PK | FK | SI | Active motility and muscle strength DR |
| Q13 | varchar | PK |  | SI | Muscle tone |
| Q13N | varchar | PK |  | SI | Note |
| Q13ObsDR | varchar | PK | FK | SI | Muscle tone DR |
| Q15 | varchar | PK |  | SI | Trophic muscle |
| Q15N | varchar | PK |  | SI | Note |
| Q15ObsDR | varchar | PK | FK | SI | Trophic muscle DR |
| Q17 | varchar | PK |  | SI | Mingazzini Test |
| Q17N | varchar | PK |  | SI | Note |
| Q17ObsDR | varchar | PK | FK | SI | Mingazzini Test DR |
| Q19 | varchar | PK |  | SI | Barre Test |
| Q19N | varchar | PK |  | SI | Note |
| Q19ObsDR | varchar | PK | FK | SI | Barre Test DR |
| Q21 | varchar | PK |  | SI | Patellar reflexes |
| Q21N | varchar | PK |  | SI | Note |
| Q21ObsDR | varchar | PK | FK | SI | Patellar reflexes DR |
| Q23 | varchar | PK |  | SI | Achilles reflexes |
| Q23N | varchar | PK |  | SI | Note |
| Q23ObsDR | varchar | PK | FK | SI | Achilles reflexes DR |
| Q25 | varchar | PK |  | SI | Radial stylus reflexes |
| Q25N | varchar | PK |  | SI | Note |
| Q25ObsDR | varchar | PK | FK | SI | Radial stylus reflexes DR |
| Q27 | varchar | PK |  | SI | Biceps reflexes |
| Q27N | varchar | PK |  | SI | Note |
| Q27ObsDR | varchar | PK | FK | SI | Biceps reflexes DR |
| Q29 | varchar | PK |  | SI | Triceps reflexes |
| Q29N | varchar | PK |  | SI | Note |
| Q29ObsDR | varchar | PK | FK | SI | Triceps reflexes DR |
| Q31 | varchar | PK |  | SI | Cutaneous reflexes |
| Q31N | varchar | PK |  | SI | Note |
| Q31ObsDR | varchar | PK | FK | SI | Cutaneous reflexes DR |
| Q33 | varchar | PK |  | SI | Cutaneous reflexes Abdominal |
| Q33N | varchar | PK |  | SI | Note |
| Q33ObsDR | varchar | PK | FK | SI | Cutaneous reflexes Abdominal DR |
| Q35 | varchar | PK |  | SI | Cutaneous reflexes plantar |
| Q35N | varchar | PK |  | SI | Note |
| Q35ObsDR | varchar | PK | FK | SI | Cutaneous reflexes plantar DR |
| Q37 | varchar | PK |  | SI | Sensibility |
| Q37N | varchar | PK |  | SI | Note |
| Q37ObsDR | varchar | PK | FK | SI | Sensibility DR |
| Q39 | varchar | PK |  | SI | Tactile Sensibility |
| Q39N | varchar | PK |  | SI | Note |
| Q39ObsDR | varchar | PK | FK | SI | Tactile Sensibility DR |
| Q41 | varchar | PK |  | SI | Thermal Sensibility |
| Q41N | varchar | PK |  | SI | Note |
| Q41ObsDR | varchar | PK | FK | SI | Thermal Sensibility DR |
| Q43 | varchar | PK |  | SI | Pallaesthesia Sensibility |
| Q43N | varchar | PK |  | SI | Note |
| Q43ObsDR | varchar | PK | FK | SI | Pallaesthesia Sensibility DR |
| Q45 | varchar | PK |  | SI | Sterognosia Sensibility |
| Q45N | varchar | PK |  | SI | Note |
| Q45ObsDR | varchar | PK | FK | SI | Sterognosia Sensibility DR |
| Q47 | varchar | PK |  | SI | Position sense Sensibility |
| Q47N | varchar | PK |  | SI | Note |
| Q47ObsDR | varchar | PK | FK | SI | Position sense Sensibility DR |
| Q49 | varchar | PK |  | SI | Cerebellar Test |
| Q49N | varchar | PK |  | SI | Note |
| Q49ObsDR | varchar | PK | FK | SI | Cerebellar Test DR |
| Q51 | varchar | PK |  | SI | Maneuver index nose |
| Q51N | varchar | PK |  | SI | Note |
| Q51ObsDR | varchar | PK | FK | SI | Maneuver index nose DR |
| Q53 | varchar | PK |  | SI | Heel knee Test |
| Q53N | varchar | PK |  | SI | Note |
| Q53NObsDR | varchar | PK | FK | SI | Note DR |
| Q53ObsDR | varchar | PK | FK | SI | Heel knee Test DR |
| Q55 | varchar | PK |  | SI | Diadochokinesis |
| Q55N | varchar | PK |  | SI | Note |
| Q55ObsDR | varchar | PK | FK | SI | Diadochokinesis DR |
| Q57 | varchar | PK |  | SI | Lasegue Test |
| Q57N | varchar | PK |  | SI | Note |
| Q57ObsDR | varchar | PK | FK | SI | Lasegue Test DR |
| Q59 | varchar | PK |  | SI | Rigor |
| Q59N | varchar | PK |  | SI | Note |
| Q59ObsDR | varchar | PK | FK | SI | Rigor DR |
| Q61 | varchar | PK |  | SI | Cranial nerves test |
| Q61N | varchar | PK |  | SI | Note |
| Q61ObsDR | varchar | PK | FK | SI | Cranial nerves test DR |
| Q63 | varchar | PK |  | SI | I Nervus olfactorius |
| Q63N | varchar | PK |  | SI | Note |
| Q63ObsDR | varchar | PK | FK | SI | I Nervus olfactorius DR |
| Q65 | varchar | PK |  | SI | II Nervus opticusolfactorius |
| Q65N | varchar | PK |  | SI | Note |
| Q65ObsDR | varchar | PK | FK | SI | II Nervus opticusolfactorius DR |
| Q67 | varchar | PK |  | SI | II Visus |
| Q67N | varchar | PK |  | SI | Note |
| Q67ObsDR | varchar | PK | FK | SI | II Visus DR |
| Q69 | varchar | PK |  | SI | II Visual field |
| Q69N | varchar | PK |  | SI | Note |
| Q69ObsDR | varchar | PK | FK | SI | II Visual field DR |
| Q71 | varchar | PK |  | SI | II Fundus |
| Q71N | varchar | PK |  | SI | Note |
| Q71ObsDR | varchar | PK | FK | SI | II Fundus DR |
| Q73 | varchar | PK |  | SI | III Nervus oculomotorius |
| Q73N | varchar | PK |  | SI | Note |
| Q73ObsDR | varchar | PK | FK | SI | III Nervus oculomotorius DR |
| Q75 | varchar | PK |  | SI | III Pupils Test |
| Q75N | varchar | PK |  | SI | Note |
| Q75ObsDR | varchar | PK | FK | SI | III Pupils Test DR |
| Q77 | varchar | PK |  | SI | IV Nervus trochealis |
| Q77N | varchar | PK |  | SI | Note |
| Q77ObsDR | varchar | PK | FK | SI | IV Nervus trochealis DR |
| Q79 | varchar | PK |  | SI | IV Pupils Test |
| Q79N | varchar | PK |  | SI | Note |
| Q79ObsDR | varchar | PK | FK | SI | IV Pupils Test DR |
| Q81 | varchar | PK |  | SI | V Nervus trigeminus |
| Q81N | varchar | PK |  | SI | Note |
| Q81ObsDR | varchar | PK | FK | SI | V Nervus trigeminus DR |
| Q83 | varchar | PK |  | SI | V Pupils Test |
| Q83N | varchar | PK |  | SI | Note |
| Q83ObsDR | varchar | PK | FK | SI | V Pupils Test DR |
| Q85 | varchar | PK |  | SI | V Extrinsic ocular motility |
| Q85N | varchar | PK |  | SI | Note |
| Q85ObsDR | varchar | PK | FK | SI | V Extrinsic ocular motility DR |
| Q87 | varchar | PK |  | SI | V Sensitive |
| Q87N | varchar | PK |  | SI | Note |
| Q87ObsDR | varchar | PK | FK | SI | V Sensitive DR |
| Q89 | varchar | PK |  | SI | VI Nervus abducens |
| Q89N | varchar | PK |  | SI | Note |
| Q89ObsDR | varchar | PK | FK | SI | VI Nervus abducens DR |
| Q91 | varchar | PK |  | SI | VII Nervus facialis |
| Q91N | varchar | PK |  | SI | Note |
| Q91ObsDR | varchar | PK | FK | SI | VII Nervus facialis DR |
| Q93 | varchar | PK |  | SI | VIII Nervus vestibulo cochlearis |
| Q93N | varchar | PK |  | SI | Note |
| Q93ObsDR | varchar | PK | FK | SI | VIII Nervus vestibulo cochlearis DR |
| Q95 | varchar | PK |  | SI | VIII Cochlear |
| Q95N | varchar | PK |  | SI | Note |
| Q95ObsDR | varchar | PK | FK | SI | VIII Cochlear DR |
| Q97 | varchar | PK |  | SI | VIII Vestibular |
| Q97N | varchar | PK |  | SI | Note |
| Q97ObsDR | varchar | PK | FK | SI | VIII Vestibular DR |
| Q99 | varchar | PK |  | SI | IX Nervus glossopharyngeus |
| Q99N | varchar | PK |  | SI | Note |
| Q99ObsDR | varchar | PK | FK | SI | IX Nervus glossopharyngeus DR |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*