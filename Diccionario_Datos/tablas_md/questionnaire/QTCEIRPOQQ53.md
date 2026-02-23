# questionnaire.QTCEIRPOQQ53

> Ingreso Recuperación : Dispositivos Invasivos

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Recuperación : Dispositivos Invasivos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q53Q1 | bit |  |  | SI | Sin Dispositivo |
| Q53Q2 | varchar |  |  | SI | Dispositivo |
| Q53Q3 | varchar |  |  | SI | Otro Dispositivo  |
| Q53Q4 | varchar |  |  | SI | Tamaño |
| Q53Q5 | varchar |  |  | SI | Ubicación |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*