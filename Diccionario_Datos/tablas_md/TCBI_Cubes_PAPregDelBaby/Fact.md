# TCBI_Cubes_PAPregDelBaby.Fact

**Schema:** TCBI_Cubes_PAPregDelBaby
**Columnas:** 46
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1113307351 | varchar |  |  | SI | Dimension: Dx1113307351<br/>
Source: BABYBirthDat... |
| Dx2093108415 | varchar |  |  | SI | Dimension: Dx2093108415<br/>
Source: BABYBirthDat... |
| Dx2930924164 | varchar |  |  | SI | Dimension: Dx2930924164<br/>
Source: BABYBirthDat... |
| Dx466251635 | varchar |  |  | SI | Dimension: Dx466251635<br/>
Source: BABYBirthDate |
| DxAbnormalities | varchar |  |  | SI | Dimension: DxAbnormalities
Expression: %cube.GetA... |
| DxAccoucheur1 | bigint |  |  | SI | Dimension: DxAccoucheur1<br/>
Source: BABYAccouch... |
| DxAccoucheur1Type | bigint |  |  | SI | Dimension: DxAccoucheur1Type<br/>
Source: BABYAcc... |
| DxAccoucheur2 | bigint |  |  | SI | Dimension: DxAccoucheur2<br/>
Source: BABYAccouch... |
| DxAccoucheur2Type | bigint |  |  | SI | Dimension: DxAccoucheur2Type<br/>
Source: BABYAcc... |
| DxAgeAtDelivery | bigint |  |  | SI | Dimension: DxAgeAtDelivery
Expression: ##class(TC... |
| DxAgeGroupAtDelivery | bigint |  |  | SI | Dimension: DxAgeGroupAtDelivery
Expression: ##cla... |
| DxApgarScore1m | bigint |  |  | SI | Dimension: DxApgarScore1m<br/>
Source: BABYApgarS... |
| DxApgarScore3 | bigint |  |  | SI | Dimension: DxApgarScore3<br/>
Source: BABYApgarSc... |
| DxApgarScore4 | bigint |  |  | SI | Dimension: DxApgarScore4<br/>
Source: BABYApgarSc... |
| DxApgarScore5m | bigint |  |  | SI | Dimension: DxApgarScore5m<br/>
Source: BABYApgarS... |
| DxBABYBirthDate | date |  |  | SI | Dimension: DxBABYBirthDate<br/>
Source: BABYBirth... |
| DxBABYBirthDateFxMonthYear | varchar |  |  | SI | Dimension: DxBABYBirthDateFxMonthYear<br/>
Source... |
| DxBABYBirthDateFxYear | varchar |  |  | SI | Dimension: DxBABYBirthDateFxYear<br/>
Source: BAB... |
| DxBirthLength | bigint |  |  | SI | Dimension: DxBirthLength<br/>
Source: BABYBirthLe... |
| DxBirthOrder | bigint |  |  | SI | Dimension: DxBirthOrder<br/>
Source: BABYBirthOrd... |
| DxBirthWeight | bigint |  |  | SI | Dimension: DxBirthWeight<br/>
Source: BABYBirthWe... |
| DxBreastFed | bigint |  |  | SI | Dimension: DxBreastFed<br/>
Source: BABYBreastFed |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: BABYDelive... |
| DxDeliveryIndication | bigint |  |  | SI | Dimension: DxDeliveryIndication
Expression: %cube... |
| DxFlyingSquad | bigint |  |  | SI | Dimension: DxFlyingSquad
Expression: %cube.BabyFl... |
| DxFormulaType | bigint |  |  | SI | Dimension: DxFormulaType<br/>
Source: BABYFormula... |
| DxGender | bigint |  |  | SI | Dimension: DxGender<br/>
Source: BABYSexDR.CTSEXD... |
| DxGestationInWeeks | bigint |  |  | SI | Dimension: DxGestationInWeeks<br/>
Source: BABYGe... |
| DxGestationInWeeksRange | bigint |  |  | SI | Dimension: DxGestationInWeeksRange<br/>
Source: B... |
| DxLiveBirth | bigint |  |  | SI | Dimension: DxLiveBirth<br/>
Source: BABYAlive |
| DxMethodNationalCode | varchar |  |  | SI | Dimension: DxMethodNationalCode
Expression: $lg(%... |
| DxMethodOfDelivery | varchar |  |  | SI | Dimension: DxMethodOfDelivery
Expression: $lg(%ex... |
| DxMethodOfFeeding | bigint |  |  | SI | Dimension: DxMethodOfFeeding<br/>
Source: BABYBab... |
| DxMidwife | bigint |  |  | SI | Dimension: DxMidwife<br/>
Source: BABYDeliveryMid... |
| DxMorbidity | varchar |  |  | SI | Dimension: DxMorbidity
Expression: %cube.GetMorbi... |
| DxMotherID | bigint |  |  | SI | Dimension: DxMotherID<br/>
Source: BABYParRef.DEL... |
| DxOutcome | bigint |  |  | SI | Dimension: DxOutcome<br/>
Source: BABYOutcomeDR.O... |
| DxOutcomeType | bigint |  |  | SI | Dimension: DxOutcomeType
Expression: %cube.GetOut... |
| DxPlaceOfDelivery | bigint |  |  | SI | Dimension: DxPlaceOfDelivery<br/>
Source: BABYAct... |
| DxPresentation | bigint |  |  | SI | Dimension: DxPresentation<br/>
Source: BABYPresen... |
| DxSkinToSkinContact | bigint |  |  | SI | Dimension: DxSkinToSkinContact<br/>
Source: BABYS... |
| DxVitGiven | bigint |  |  | SI | Dimension: DxVitGiven<br/>
Source: BABYVitKGiven |
| RxIDViaBABYParRef | bigint |  |  | SI | Relationship: RxIDViaBABYParRef<br/>
Source: BABY... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*