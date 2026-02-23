# SQLUser.AR_CreditCardPayments

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARD_RowId | bigint | PK |  | NO | - |
| CARD_Amount | double |  |  | SI | Amount |
| CARD_Card_DR | bigint |  | FK | SI | Des Ref Card |
| CARD_Date | date |  |  | SI | Date |
| CARD_Time | time |  |  | SI | Time |
| CARD_User_DR | bigint |  | FK | SI | Des Ref User |
| Q26Q1 | - |  |  | SI | Localización |
| Q26Q2 | - |  |  | SI | Otra parte del cuerpo |
| Q26Q3 | - |  |  | SI | Clasificación Benaim |
| Q26Q4 | - |  |  | SI | Otra Clasificación |
| Q26Q5 | - |  |  | SI | Índice de Gravedad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*