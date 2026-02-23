# TCBI_Cubes_PALetter.Fact

**Schema:** TCBI_Cubes_PALetter
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1771795776 | varchar |  |  | SI | Dimension: Dx1771795776<br/>
Source: LETLastPrint... |
| Dx2394466956 | varchar |  |  | SI | Dimension: Dx2394466956<br/>
Source: LETCreateDat... |
| Dx2720349257 | varchar |  |  | SI | Dimension: Dx2720349257<br/>
Source: LETLastPrint... |
| Dx2766697603 | varchar |  |  | SI | Dimension: Dx2766697603<br/>
Source: LETCreateDat... |
| Dx3058968535 | varchar |  |  | SI | Dimension: Dx3058968535<br/>
Source: LETCreateDat... |
| Dx3142594760 | varchar |  |  | SI | Dimension: Dx3142594760<br/>
Source: LETUpdateDat... |
| Dx3580631440 | varchar |  |  | SI | Dimension: Dx3580631440<br/>
Source: LETUpdateDat... |
| Dx3949369855 | varchar |  |  | SI | Dimension: Dx3949369855<br/>
Source: LETUpdateDat... |
| Dx765914329 | varchar |  |  | SI | Dimension: Dx765914329<br/>
Source: LETLastPrintD... |
| Dx920508871 | varchar |  |  | SI | Dimension: Dx920508871<br/>
Source: LETLastPrintD... |
| DxLETCreateDate | date |  |  | SI | Dimension: DxLETCreateDate<br/>
Source: LETCreate... |
| DxLETCreateDateFxMonthYear | varchar |  |  | SI | Dimension: DxLETCreateDateFxMonthYear<br/>
Source... |
| DxLETCreateDateFxYear | varchar |  |  | SI | Dimension: DxLETCreateDateFxYear<br/>
Source: LET... |
| DxLETLastPrintDate | date |  |  | SI | Dimension: DxLETLastPrintDate<br/>
Source: LETLas... |
| DxLETLastPrintDateFxYear | varchar |  |  | SI | Dimension: DxLETLastPrintDateFxYear<br/>
Source: ... |
| DxLETUpdateDate | date |  |  | SI | Dimension: DxLETUpdateDate<br/>
Source: LETUpdate... |
| DxLETUpdateDateFxMonthYear | varchar |  |  | SI | Dimension: DxLETUpdateDateFxMonthYear<br/>
Source... |
| DxLETUpdateDateFxYear | varchar |  |  | SI | Dimension: DxLETUpdateDateFxYear<br/>
Source: LET... |
| DxLetterCategory | bigint |  |  | SI | Dimension: DxLetterCategory<br/>
Source: LETCTLet... |
| DxLetterTemplate | bigint |  |  | SI | Dimension: DxLetterTemplate<br/>
Source: LETCTLet... |
| DxLetterType | bigint |  |  | SI | Dimension: DxLetterType<br/>
Source: LETLetterTyp... |
| DxPrintedBy | bigint |  |  | SI | Dimension: DxPrintedBy<br/>
Source: LETLastPrintU... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus
Expression: ##class(TCBI.Util... |
| RxIDViaLETPAADMDR | bigint |  | FK | SI | Relationship: RxIDViaLETPAADMDR<br/>
Source: LETP... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*